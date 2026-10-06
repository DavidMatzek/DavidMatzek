# Mini Cases

[Back to Overview](README.md)

Each case leads with the result, followed by the situation and approach that
produced it.

## Featured Case: AI-Agent Automation for Vehicle Signal Specification (VSS) Data Model Governance

Result: Daily operations dropped from an effective workload equivalent to
about 20 hours/day to about 35 minutes/day for a 240+ consumer data model.
Automated away governance work equivalent to ~3 full-time employees
(~€350k/year fully-loaded cost) while serving 45+ regular contributors,
sustaining a weekly release cadence with far less manual review overhead. A
metadata self-service page requested since 2020 was delivered in 20
workdays, contractor dependency dropped, and freed capacity was redirected
to other budget-constrained projects — all delivered in parallel with a
strategic `.vspec` → GraphQL (S2DM) data-model migration for the same 180+
consumer applications.

Role Context:

Data Steward and Data Model Owner (01/2025 - Present), owner of BMW's VSS
(Vehicle Signal Specification) data model backing the Vehicle Shadow stream,
consumed by 180+ backend applications, with stewardship of historized
petabyte-scale data.

Situation:

From January 2026, a critical data-model operation had to continue after
staffing changes and consultant budget cuts (the previous setup relied on
one internal owner plus two external consultants). At the same time,
maintaining the VSS repo required manual PR review and labeling, board
triage, release orchestration, and CI-failure fixing. Every contributor
needed GitHub write access and had to author a pull request themselves —
non-technical stakeholders couldn't contribute at all without engineering
support.

Team Goal:

- Keep operations stable while reducing cost and overhead.
- Remove governance overhead consuming the equivalent of ~3 FTEs.
- Remove the git/PR literacy barrier for non-technical contributors.
- Build a support model that scales without contractor dependency.
- Keep a sustained weekly release cadence, run alongside the ongoing
  `.vspec` → GraphQL (S2DM) migration.

What Was Implemented (from 01/2026):

- Focus on the core earning process first; refactor the underlying data
  model for reliability and maintainability.
- 7 purpose-built AI agents (contribution, board/PM, release, CI-fixer,
  PR-creator, explorer-data, explorer-dev) orchestrating ~15 reusable
  skills — auto-triage CI failures, auto-rebase conflicting branches,
  auto-classify legal (EU Data Act) requirements, auto-generate changelogs
  and version bumps, auto-sort the Kanban release board.
- A self-service web UI ("VSS Explorer") replacing the PR-only contribution
  model: wizards let contributors without repo access submit signal
  requests and classifications directly; a backend pipeline converts these
  into structured GitHub issues and auto-generates compliant PRs, removing
  the git/PR literacy barrier entirely.
- Bulk content-quality automation: a linter plus LLM rewriter for spec
  descriptions, benchmarked across 3 model tiers to pick the most
  cost-efficient option at equal quality — a deliberate cost/performance
  tradeoff, not just "use the biggest model."

Reusable Method:

- Protect value creation first, automate overhead second.
- Design agent architecture around discrete, reusable skills rather than one
  monolithic agent.
- Remove access barriers with self-service UX instead of only speeding up
  the existing process; let users resolve standard issues themselves.
- Treat model and tool selection as a cost/performance engineering decision.
- Run automation delivery in parallel with ongoing operations and a
  multi-year architecture migration, not as a separate side project.

---

## Venture (in progress): Tender-to-Invoice Automation for the Mittelstand

Status: In progress (from 2026). Landing-page showcase; kept out of the formal CV.

Result (target): A product that removes the manual tender-handling burden for
mid-sized trades — screening German public tenders (Ausschreibungen),
drafting offers (Angebote), and issuing invoices (Rechnungen) from one guided
workflow.

Situation:

Electricians, facility management, security, and construction firms spend
scarce back-office time manually screening tender portals, re-keying offer
documents, and preparing invoices — repetitive, rule-based, error-prone work.

What Is Being Built:

- Automated screening and relevance-ranking of incoming Ausschreibungen.
- Assisted Angebotserstellung (offer generation) from reusable templates and
  past bids.
- One-click Rechnung setup feeding into existing accounting.

Reusable Method:

- Apply agentic automation to a concrete, high-friction business workflow.
- Remove the literacy barrier with guided UX, as in prior self-service work.

---

## Case: Decision & Check Automation (Vehicle Functions to Production Lines)

Result: Three patent specifications for automating vehicle decisions and
configurations — rule- and event-driven automation that decides and acts
without manual intervention — backed by MBSE-based automated validation and a
production-line engineering foundation.

Situation:

Customer-facing vehicle functions required decisions and state changes to be
automated safely, and their behavior to be verified automatically rather than
by manual checking.

What Was Implemented:

- Event- and rule-driven automation of vehicle functions and state changes
  (window control, function configuration), captured in patent specifications.
- MBSE models as the single source of truth, enabling generated, automated
  checks across design, implementation, and testing.
- Engineering foundation from a production-line apprenticeship, informing
  where automated decisions and quality checks add the most value.

Reusable Method:

- Encode decisions as explicit, testable rules and events.
- Automate the checks, not just the actions, through model-based generation.

---

## Case: First Standardized Service Interface in BMW E/E Architecture

Result: First standardized interface for a low-level vehicle function,
enabling uniform window-control behavior across BMW Group brands and a
reusable blueprint for decoupled, data-centric interfaces.

Situation:

Vehicle-function architecture was highly coupled, with safety-critical
dependencies and legacy communication buses.

Team Goal:

Enable higher-level functions such as speech interaction and automation to
control window movement without exposing functional logic or safety logic.

What Was Implemented:

- Strict service abstraction separating window control from safety internals.
- Standardized interface for movement requests, availability, and position semantics.
- Information-hiding rules for reuse across brands and derivatives.

---

## Case: Middleware for Standardized Vehicle Data

Result: Standardized vehicle data usage scaled across derivatives, cutting
re-implementation effort and integration friction, and letting teams shift
focus from reconciliation work to feature development.

Situation:

Vehicle networks were heterogeneous and continuously changing, creating
high variant dependency and low semantic consistency.

Team Goal:

Abstract low-level vehicle data into a stable semantic model (VSS by COVESA)
despite evolving systems, organizational friction, and changing standards.

What Was Implemented:

- MBSE mapping model as single source of truth.
- Machine-readable outputs and generator-based integration for derivatives.
- Controlled extension strategy while preserving standard alignment.
- End-to-end validation via generation, simulation, and analytics.

---

## Case: Intelligent Functions from Concept to Series Release

Result: Two customer-facing functions reached series release in 2019,
generating two patent specifications and increased portfolio value through
sustained usage and conversion impact.

Situation:

An intelligent-function initiative faced high customer expectations, complex
stakeholder requirements, late start, and tight budget.

Team Goal:

- Deliver committed customer value under tight constraints.
- Keep alignment across safety, privacy, UX, validation, and production.

What Was Implemented:

- Delivery focus on customer value without political drift.
- Tight cross-functional technical coordination.
- MBSE to align understanding across design, implementation, and testing.

---

## Case: Data Middleware Adoption Through Trust and Automation

Result: Middleware was integrated into the Neue Klasse E/E architecture,
giving teams a scalable path to consistent data across derivatives and
initiating a patent specification from the solution direction.

Situation:

Need for standardized in-vehicle and backend data was clear, but ownership,
acceptance, and implementation commitment were weak.

Team Goal:

- Build cross-department commitment to a common architecture direction.
- Create an implementation path teams can actually adopt.

What Was Implemented:

- Transparent collaboration and trust building across departments.
- Architecture and testing strategy validation with COVESA specialists.
- Middleware embedded into existing data-collection framework for broad impact.
- MBSE linkage to board-network sources and VSS.
- Generator-based delivery and transparent automated testing.

---

## Current Case: Ontology-Based Evolution of Standardization Language

Status: In progress. Target result is a governance model that stays close to
domain knowledge and supports future AI use cases without reducing model
clarity.

Role Context:

Data Steward and Data Model Owner (01/2025 - Present).

Situation:

Tree-based structures limit governance simplicity and semantic richness needed
for future AI-enabled workflows.

Team Goal:

- Improve governance close to domain knowledge.
- Support future AI use cases without reducing model clarity.

Current Direction:

- Architecture and governance design for model evolution.
- Close collaboration with COVESA participants.
