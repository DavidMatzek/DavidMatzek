<#
.SYNOPSIS
  Build everything: site HTML (EN/DE), CV sources, CV PDFs, and copy PDFs into site/assets.

.EXAMPLE
  ./tools/build.ps1          # site + both CVs
  ./tools/build.ps1 -Png     # also render PNG previews of the CVs
  ./tools/build.ps1 -SiteOnly
#>
param(
    [switch]$Png,
    [switch]$SiteOnly
)
$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot -Parent
$py = Join-Path $root '.venv/Scripts/python.exe'
if (-not (Test-Path $py)) { throw "venv python not found at $py (python -m venv .venv; .venv/Scripts/pip install -r requirements.txt)" }

& $py (Join-Path $PSScriptRoot 'build.py')
if ($LASTEXITCODE -ne 0) { throw "tools/build.py failed (exit $LASTEXITCODE)" }
if ($SiteOnly) { return }

# Keep in sync with content/data.yaml (site.cv_pdf).
$targets = @{ en = 'David-Matzek-CV.pdf'; de = 'David-Matzek-CV-DE.pdf' }
foreach ($lang in $targets.Keys) {
    $tex = Join-Path $root "cv/generated/cv-$lang.tex"
    if ($Png) { & (Join-Path $PSScriptRoot 'build-cv.ps1') -Tex $tex -Png } else { & (Join-Path $PSScriptRoot 'build-cv.ps1') -Tex $tex }
    Copy-Item ([System.IO.Path]::ChangeExtension($tex, 'pdf')) (Join-Path $root "site/assets/$($targets[$lang])") -Force
}
