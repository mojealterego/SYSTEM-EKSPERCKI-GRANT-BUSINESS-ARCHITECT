from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class EvidenceKind(StrEnum):
    FACT = "fact"
    ASSUMPTION = "assumption"
    INFERENCE = "inference"
    MISSING = "missing"


class Confidence(StrEnum):
    VERIFIED = "verified"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    UNKNOWN = "unknown"


class Severity(StrEnum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    BLOCKER = "blocker"


class Stage(StrEnum):
    V0_CONCEPT = "V0_CONCEPT"
    V1_MARKET = "V1_MARKET"
    V2_BUSINESS_MODEL = "V2_BUSINESS_MODEL"
    V3_FINANCE = "V3_FINANCE"
    V4_BUDGET = "V4_BUDGET"
    V5_APPLICATION = "V5_APPLICATION"
    V6_BUSINESS_PLAN = "V6_BUSINESS_PLAN"
    V7_COMPLIANCE = "V7_COMPLIANCE"
    V8_RED_TEAM = "V8_RED_TEAM"
    V9_FINAL = "V9_FINAL"


@dataclass(frozen=True)
class Evidence:
    id: str
    kind: EvidenceKind
    statement: str
    source: str | None = None
    source_date: str | None = None
    citation: str | None = None
    confidence: Confidence = Confidence.UNKNOWN
    limitations: str | None = None


@dataclass(frozen=True)
class Finding:
    id: str
    severity: Severity
    title: str
    detail: str
    evidence_ids: tuple[str, ...] = ()
    remediation: str | None = None


@dataclass
class ProjectState:
    project_id: str
    version: str = "V0.0"
    stage: Stage = Stage.V0_CONCEPT
    language: str = "pl-PL"
    applicant: dict[str, Any] = field(default_factory=dict)
    project: dict[str, Any] = field(default_factory=dict)
    funding_options: list[dict[str, Any]] = field(default_factory=list)
    business_model: dict[str, Any] = field(default_factory=dict)
    product: dict[str, Any] = field(default_factory=dict)
    operations: dict[str, Any] = field(default_factory=dict)
    pricing: dict[str, Any] = field(default_factory=dict)
    financials: dict[str, Any] = field(default_factory=dict)
    budget: list[dict[str, Any]] = field(default_factory=list)
    metrics: list[dict[str, Any]] = field(default_factory=list)
    risks: list[dict[str, Any]] = field(default_factory=list)
    documents: dict[str, Any] = field(default_factory=dict)
    evidence: dict[str, Evidence] = field(default_factory=dict)
    findings: list[Finding] = field(default_factory=list)
    missing_data: dict[str, list[str]] = field(default_factory=lambda: {"critical": [], "important": [], "optional": []})
    metadata: dict[str, Any] = field(default_factory=dict)
