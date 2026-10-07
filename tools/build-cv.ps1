<#
.SYNOPSIS
  Build a LaTeX CV to PDF with Tectonic, optionally rendering PNG previews.

.EXAMPLE
  ./tools/build-cv.ps1 -Tex cv/generated/cv-en.tex -Png
#>
param(
    [Parameter(Mandatory = $true)][string]$Tex,
    [switch]$Png,
    [int]$Dpi = 150
)
$ErrorActionPreference = 'Stop'

# Auto-detect a corporate proxy (honoring the system PAC) if not already set.
if (-not $env:HTTPS_PROXY) {
    try {
        $probe = [System.Net.WebRequest]::GetSystemWebProxy().GetProxy([uri]'https://ctan.org').AbsoluteUri
        if ($probe -and $probe -notmatch 'ctan\.org') {
            $env:HTTP_PROXY = $probe
            $env:HTTPS_PROXY = $probe
        }
    }
    catch {}
}

$root = Split-Path $PSScriptRoot -Parent
$tectonic = Join-Path $PSScriptRoot 'bin/tectonic.exe'
if (-not (Test-Path $tectonic)) { throw "Tectonic not found at $tectonic" }

$texPath = (Resolve-Path $Tex).Path
$outdir = Split-Path $texPath -Parent

& $tectonic $texPath --outdir $outdir
if ($LASTEXITCODE -ne 0) { throw "Tectonic failed (exit $LASTEXITCODE)" }

$pdf = [System.IO.Path]::ChangeExtension($texPath, 'pdf')
Write-Host "PDF: $pdf"

if ($Png) {
    $vpy = Join-Path $root '.venv/Scripts/python.exe'
    if (-not (Test-Path $vpy)) { throw "venv python not found at $vpy" }
    & $vpy (Join-Path $PSScriptRoot 'render_pdf.py') $pdf $outdir $Dpi
}
