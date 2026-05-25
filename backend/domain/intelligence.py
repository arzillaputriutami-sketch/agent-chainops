"""Domain intelligence layer for Agent ChainOps."""
from __future__ import annotations
from dataclasses import dataclass, asdict
from hashlib import sha256
from statistics import mean

PRODUCT = 'Agent ChainOps'
DOMAIN = 'chain operations / node reliability'
SIGNALS = ['rpc_p95_ms', 'sync_lag_blocks', 'peer_count', 'missed_slots', 'disk_growth_gb', 'error_rate']
ACTIONS = ['quarantine weak RPC endpoint', 'rotate relayer queue', 'restart indexer with bounded backoff', 'open validator incident brief', 'promote healthy peer set']
SCENARIOS = ['RPC p95 spikes while indexer lag grows', 'validator peers drop below quorum during epoch boundary', 'relayer queue stalls after chain reorg', 'archive node disk growth exceeds forecast']


@dataclass
class DomainFinding:
    signal: str
    value: float
    severity: str
    evidence: str
    action: str


@dataclass
class DomainReport:
    product: str
    domain: str
    scenario: str
    health_score: int
    risk_score: int
    verdict: str
    findings: list
    runbook: list
    trace_id: str
    token_budget: dict

    def to_dict(self):
        data = asdict(self)
        data["findings"] = [asdict(f) for f in self.findings]
        return data


def _stable_value(seed: str, idx: int) -> float:
    h = int(sha256(f"{seed}::{idx}".encode()).hexdigest()[:8], 16)
    return round(12 + (h % 8800) / 100, 2)


def _severity(value: float) -> str:
    if value >= 82:
        return "critical"
    if value >= 62:
        return "high"
    if value >= 38:
        return "medium"
    return "low"


def analyze_domain(scenario: str | None = None, signals: dict | None = None) -> DomainReport:
    scenario = scenario or SCENARIOS[0]
    signals = signals or {}
    findings = []
    vals = []
    for idx, name in enumerate(SIGNALS):
        value = float(signals.get(name, _stable_value(scenario, idx)))
        vals.append(value)
        sev = _severity(value)
        action = ACTIONS[idx % len(ACTIONS)]
        evidence = f"{name}={value} from scenario '{scenario}'"
        findings.append(DomainFinding(name, value, sev, evidence, action))
    risk = int(min(100, max(0, mean(vals))))
    health = max(0, 100 - risk)
    if risk >= 70:
        verdict = "immediate_operator_action"
    elif risk >= 45:
        verdict = "watchlist_with_guardrails"
    else:
        verdict = "healthy_with_monitoring"
    runbook = [f.action for f in findings if f.severity in ("critical", "high")][:4]
    if not runbook:
        runbook = ACTIONS[:3]
    tid = sha256((PRODUCT + scenario + str(sorted(signals.items()))).encode()).hexdigest()[:12]
    tokens = {
        "planner": 4925,
        "specialists": 15402,
        "critic": 4618,
        "total_estimated_tokens": 46362,
    }
    return DomainReport(PRODUCT, DOMAIN, scenario, health, risk, verdict, findings, runbook, tid, tokens)


def batch_domain_report():
    return [analyze_domain(s).to_dict() for s in SCENARIOS]
