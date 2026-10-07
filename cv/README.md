# CV Generation System

This folder contains templates and output conventions for role-specific CV creation.

## Goal
Use one canonical profile source to produce multiple targeted CV versions aligned to job requirements.

## Process
1. Add a target role brief in targets/job-searches/ using the provided template.
2. Match requirements against profile/master/profile.yaml and profile/evidence/highlights.md.
3. Generate a tailored CV using cv/templates/cv-tailoring-template.md.
4. Save final output in cv/generated/ with standardized naming.

## Bilingual site and 2-page CV (EN/DE)
The landing page and the 2-page CV are generated from one content source:

- `content/data.yaml`: language-neutral facts (dates, ids, URLs).
- `content/en.yaml`, `content/de.yaml`: all translatable text; identical key structure (checked by the build).
- `templates/site/index.html.j2`, `templates/cv/cv.tex.j2`: one template per artifact. Layout lives in `site/assets/style.css` and `cv/templates/cv-template.tex`.

Build: `./tools/build.ps1` (`-Png` for CV previews, `-SiteOnly` for HTML only). Outputs are generated and not committed: `site/index.html`, `site/de/index.html`, `cv/generated/cv-{en,de}.tex`, and the PDFs in `site/assets/`. CI (`.github/workflows/pages.yml`) rebuilds them and fails if a CV is not exactly 2 pages.

Setup once: `python -m venv .venv; .venv/Scripts/pip install -r requirements.txt`.

## Output Naming Convention
Use this filename pattern:

YYYY-MM-DD_company_role_location_version.md

Example:

2026-08-03_companyX_senior-data-architect_munich_v1.md

## Quality Gate Before Export
- Role title and summary directly match the target role language.
- Top 5 requirements are explicitly reflected in experience bullets.
- Keywords for ATS are included naturally, not stuffed.
- Bullets are impact-oriented and include scope/context where possible.
- Document length fits target format (one-page or two-page variant).
