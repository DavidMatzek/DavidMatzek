# CV Generation System

This folder contains templates and output conventions for role-specific CV creation.

## Goal
Use one canonical profile source to produce multiple targeted CV versions aligned to job requirements.

## Process
1. Add a target role brief in targets/job-searches/ using the provided template.
2. Match requirements against profile/master/profile.yaml and profile/evidence/highlights.md.
3. Generate a tailored CV using cv/templates/cv-tailoring-template.md.
4. Save final output in cv/generated/ with standardized naming.

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
