# Repository Handover Guide

This repository is structured as a professional profile system that supports fast generation of role-specific CVs.

## What this repository is
- A single source of truth for profile data and evidence.
- A repeatable system for tailoring CVs per job search.
- A recruiter-ready profile repository that can be shared directly.

## Folder Responsibilities
- profile/master/: canonical structured profile content.
- profile/evidence/: supporting cases, patents, and proof points.
- targets/job-searches/: captured role requirements for each application.
- cv/templates/: templates for drafting CV variants.
- cv/generated/: finalized, role-specific CV outputs.
- Documents/: optional exported PDF versions.

## Operating Workflow
1. Capture role requirements with targets/job-searches/job-requirements-template.md.
2. Select matching strengths and evidence from profile/master and profile/evidence.
3. Draft the role-specific CV using cv/templates/cv-tailoring-template.md.
4. Save markdown output in cv/generated/.
5. Export PDF to Documents/ when needed.

## Notes for Direct Sharing
- Keep README.md as the main entry point.
- Keep generated CV filenames consistent for easy navigation.
- Keep profile/master/profile.yaml updated first; other outputs derive from it.
