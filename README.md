# GRANT & BUSINESS ARCHITECT

Production-oriented multi-agent AI system for designing defensible business plans, funding strategies, grant applications, budgets and audit-ready evidence packages.

## Design principles
- Evidence before prose.
- No fabricated facts, laws, deadlines, prices, contracts or credentials.
- Program-specific eligibility is isolated by funding source.
- Every material claim can be traced to evidence, assumption or missing-data status.
- Separate generation from adversarial review.
- Cross-document consistency is a first-class invariant.
- Financial outputs are deterministic and testable.
- Human approval gates protect consequential submissions.

## Agent topology

```text
User / Client
    |
    v
Intake & Interview Agent
    |
    v
Project State / Evidence Ledger <---- Research & Source Agent
    |                                   |
    +---- Funding Intelligence Agent ---+
    |
    +---- Eligibility & Compliance Agent
    |
    +---- Market & Competition Agent
    |
    +---- Business Model Agent
    |
    +---- Product & Operations Agent
    |
    +---- Pricing & Unit Economics Agent
    |
    +---- Financial Model Agent
    |
    +---- Grant Budget Agent
    |
    +---- Metrics & Risk Agent
    |
    v
Document Assembly Agent
    |
    v
Cross-Consistency Validator
    |
    +---- Formal Compliance Auditor
    +---- Reviewer / Scoring Agent
    +---- Adversarial Red Team
    |
    v
Finalization Gate -> exportable package
```

## Repository map

- `apps/` runtime entrypoints and API surface
- `packages/core/` domain models, contracts, state and orchestration
- `packages/agents/` specialist agent definitions and prompts
- `packages/tools/` web/source, finance, documents and validation tools
- `packages/scoring/` criterion mapping and reviewer simulation
- `packages/audit/` compliance, provenance and red-team engines
- `prompts/` versioned system prompts and policies
- `schemas/` JSON Schemas / machine contracts
- `fixtures/` synthetic projects and deterministic test data
- `tests/` unit, integration and invariant tests
- `.github/workflows/` CI quality gates
- `docs/` architecture, threat model, ADRs and runbooks

## Status

Bootstrap architecture. Core contracts and implementation follow in small, reviewable commits.

## Source basis

The initial operating doctrine is derived from the supplied **MASTER PROMPT — AI ARCHITEKT BIZNESPLANÓW I WNIOSKÓW DOTACYJNYCH** and expanded into executable system contracts. The source specifically requires staged work, current official sources for rules, evidence-backed claims, explicit missing-data states, financial modelling, compliance review and red-team review.
