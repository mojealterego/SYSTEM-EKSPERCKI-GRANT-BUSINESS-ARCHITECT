from dataclasses import dataclass

@dataclass(frozen=True)
class AgentSpec:
    id: str
    name: str
    mission: str
    inputs: tuple[str, ...]
    outputs: tuple[str, ...]
    stage: str
    risk_class: str = "analysis"
    allowed_tools: tuple[str, ...] = ()
    requires_human_approval: bool = False

AGENTS = (
    AgentSpec("chief_architect", "Chief Architect", "Orchestrate workflow and enforce policy.", ("project_state",), ("plan",), "all", "control"),
    AgentSpec("intake", "Intake & Interview", "Collect highest-value missing information.", ("user_input",), ("applicant_profile", "missing_data"), "V0_CONCEPT"),
    AgentSpec("funding_intelligence", "Funding Intelligence", "Identify current funding paths using authoritative sources.", ("project_state",), ("funding_options", "source_ledger"), "V0_CONCEPT", "research", ("web",)),
    AgentSpec("eligibility", "Eligibility & Compliance", "Determine program-specific eligibility and exclusions.", ("funding_options", "project_state"), ("eligibility_matrix",), "V0_CONCEPT", "compliance"),
    AgentSpec("market", "Market & Competition", "Validate demand, segments and competition.", ("project_state",), ("market_analysis", "competition"), "V1_MARKET", "research", ("web",)),
    AgentSpec("business_model", "Business Model Architect", "Design coherent value proposition and economics.", ("market_analysis", "applicant_profile"), ("business_model",), "V2_BUSINESS_MODEL"),
    AgentSpec("product_ops", "Product & Operations", "Translate product into realizable operations.", ("business_model",), ("product", "operations"), "V2_BUSINESS_MODEL"),
    AgentSpec("pricing", "Pricing & Unit Economics", "Build cost-backed pricing and unit economics.", ("product", "operations"), ("pricing",), "V3_FINANCE"),
    AgentSpec("finance", "Financial Modeler", "Build reproducible forecasts and scenarios.", ("pricing", "operations"), ("financials",), "V3_FINANCE"),
    AgentSpec("budget", "Grant Budget Architect", "Construct and defend program-aligned budget.", ("eligibility_matrix", "financials", "operations"), ("budget",), "V4_BUDGET"),
    AgentSpec("metrics_risk", "Metrics & Risk", "Design measurable KPIs and risk register.", ("financials", "operations", "funding_options"), ("metrics", "risks"), "V4_BUDGET"),
    AgentSpec("document", "Document Assembly", "Assemble artifacts only from approved state.", ("project_state",), ("documents",), "V5_APPLICATION"),
    AgentSpec("consistency", "Cross-Consistency Validator", "Detect contradictions across all artifacts.", ("project_state",), ("findings",), "V7_COMPLIANCE", "audit"),
    AgentSpec("formal_audit", "Formal Compliance Auditor", "Audit dates, limits, attachments and rules.", ("project_state",), ("findings",), "V7_COMPLIANCE", "audit"),
    AgentSpec("reviewer", "Reviewer & Scoring", "Simulate evaluation against published criteria.", ("project_state",), ("scorecard", "findings"), "V8_RED_TEAM", "audit"),
    AgentSpec("red_team", "Adversarial Red Team", "Attack the proposal for rejection and score-loss vectors.", ("project_state", "scorecard"), ("findings",), "V8_RED_TEAM", "adversarial"),
    AgentSpec("final_gate", "Final Gate", "Block release when critical conditions fail.", ("project_state", "findings"), ("release_decision",), "V9_FINAL", "control", requires_human_approval=True),
)
