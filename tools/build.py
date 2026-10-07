"""Render the landing page and CV sources for every language from content/*.yaml.

content/data.yaml    language-neutral facts (dates, ids, URLs)
content/<lang>.yaml  all translatable text, identical key structure per language
templates/           one Jinja2 template per artifact (site HTML, CV LaTeX)

Outputs (generated, not committed):
  site/index.html, site/de/index.html
  cv/generated/cv-en.tex, cv/generated/cv-de.tex
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
TEMPLATES = ROOT / "templates"
LANGS = ["en", "de"]

# ---------------------------------------------------------------- inline markup
# Content strings may use **bold** and [text](url); each output format renders them itself.
_TOKEN = re.compile(r"\*\*(.+?)\*\*|\[([^\]]+)\]\(([^)]+)\)")


def _render(s: str, fmt) -> str:
    out, pos = [], 0
    for m in _TOKEN.finditer(s):
        out.append(fmt.text(s[pos:m.start()]))
        if m.group(1) is not None:
            out.append(fmt.bold(_render(m.group(1), fmt)))
        else:
            out.append(fmt.link(_render(m.group(2), fmt), m.group(3)))
        pos = m.end()
    out.append(fmt.text(s[pos:]))
    return "".join(out)


class Html:
    text = staticmethod(lambda s: html.escape(s, quote=False))
    bold = staticmethod(lambda s: f"<strong>{s}</strong>")

    @staticmethod
    def link(label: str, url: str) -> str:
        rel = ' rel="noopener"' if url.startswith("http") else ""
        return f'<a href="{html.escape(url)}"{rel}>{label}</a>'


_TEX_CHARS = {
    "\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "&": r"\&", "%": r"\%",
    "$": r"\$", "#": r"\#", "_": r"\_", "^": r"\textasciicircum{}", "~": r"\textasciitilde{}", "|": r"\textbar{}",
    "\u00a0": "~", "\u2009": r"\,", "\u200a": r"\,",
    "—": r"\textemdash{}", "–": "--", "→": r"$\to$", "×": r"$\times$", "·": r"\textperiodcentered{}",
}


def tex_escape(s: str) -> str:
    return "".join(_TEX_CHARS.get(c, c) for c in s)


def tex_url(url: str) -> str:
    return url.replace("%", r"\%").replace("#", r"\#")


class Tex:
    text = staticmethod(tex_escape)
    bold = staticmethod(lambda s: r"\textbf{" + s + "}")

    @staticmethod
    def link(label: str, url: str) -> str:
        return r"\href{" + tex_url(url) + "}{" + label + "}"


# ---------------------------------------------------------------- content loading
def load_yaml(path: Path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def check_parity(a, b, path: str = "") -> list[str]:
    """Return differences in key structure / list length between two language trees."""
    problems: list[str] = []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b), key=str):
            if k not in a:
                problems.append(f"{path}/{k}: missing in en")
            elif k not in b:
                problems.append(f"{path}/{k}: missing in de")
            else:
                problems += check_parity(a[k], b[k], f"{path}/{k}")
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            problems.append(f"{path}: list length en={len(a)} de={len(b)}")
        for i, (x, y) in enumerate(zip(a, b)):
            problems += check_parity(x, y, f"{path}[{i}]")
    elif type(a) is not type(b):
        problems.append(f"{path}: type en={type(a).__name__} de={type(b).__name__}")
    elif isinstance(b, str) and not b.strip():
        problems.append(f"{path}: empty string in de")
    return problems


def espacenet(pn: str) -> str:
    return f"https://worldwide.espacenet.com/patent/search?q=pn%3D{pn}"


# ---------------------------------------------------------------- rendering
def make_env(tex: bool) -> Environment:
    common = dict(
        loader=FileSystemLoader(str(TEMPLATES)),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
        autoescape=False,
    )
    if tex:  # LaTeX uses {} and % heavily, so use distinct delimiters
        env = Environment(
            block_start_string="<%", block_end_string="%>",
            variable_start_string="<<", variable_end_string=">>",
            comment_start_string="<#", comment_end_string="#>",
            **common,
        )
        env.filters["x"] = lambda s: _render(s, Tex)
        env.filters["xurl"] = tex_url
    else:
        env = Environment(**common)
        env.filters["h"] = lambda s: _render(s, Html)
        env.filters["attr"] = lambda s: html.escape(s, quote=True)
    env.globals["espacenet"] = espacenet
    return env


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    print(f"wrote {path.relative_to(ROOT)}")


def main() -> int:
    data = load_yaml(CONTENT / "data.yaml")
    trees = {lang: load_yaml(CONTENT / f"{lang}.yaml") for lang in LANGS}

    problems = check_parity(trees["en"], trees["de"])
    if problems:
        print("Translation parity errors:", *problems, sep="\n  ")
        return 1

    html_env, tex_env = make_env(tex=False), make_env(tex=True)
    base = data["site"]["base_url"]
    for lang in LANGS:
        is_en = lang == "en"
        prefix = "" if is_en else "../"
        ctx = dict(
            lang=lang, t=trees[lang], d=data, prefix=prefix,
            page_url=base if is_en else base + "de/",
            lang_links={"en": "./" if is_en else "../", "de": "de/" if is_en else "./"},
            cv_href=f"{prefix}assets/{data['site']['cv_pdf'][lang]}",
        )
        out = html_env.get_template("site/index.html.j2").render(**ctx)
        write(ROOT / "site" / ("index.html" if is_en else "de/index.html"), out)

        out = tex_env.get_template("cv/cv.tex.j2").render(
            lang=lang, t=trees[lang], d=data, babel=None if is_en else "ngerman",
        )
        write(ROOT / "cv" / "generated" / f"cv-{lang}.tex", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
