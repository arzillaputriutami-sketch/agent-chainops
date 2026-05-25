"""Domain-specific specialist agents for ChainOps Commander.

These agents are deterministic stand-ins for reviewer demos and can be swapped to
MiMo API calls through backend.core.mimo_client.MiMoClient.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any, Dict, List
import hashlib

@dataclass
class AgentFinding:
    agent: str
    role: str
    severity: str
    confidence: float
    finding: str
    evidence: List[str]
    recommendation: str
    estimated_tokens: int

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

SPECIALISTS = [('RPC Health Probe', 'measures latency, error rates, and block freshness across endpoints'), ('Sync Drift Analyst', 'detects stalled peers, fork risk, and lagging validators'), ('Capacity Planner', 'projects CPU/RAM/disk pressure from telemetry trends'), ('Runbook Writer', 'generates concrete operator remediation steps'), ('SLA Reporter', 'summarizes uptime, risk, and response priority')]

SEVERITIES = ["low", "medium", "high", "critical"]

def _score(seed: str, idx: int) -> int:
    h = hashlib.sha256(f"{seed}:{idx}".encode()).hexdigest()
    return int(h[:8], 16)

def run_specialist_agents(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    subject = str(payload.get("subject") or payload.get("scenario") or payload.get("input") or "validator RPC latency rises while block height lags peers")
    findings: List[AgentFinding] = []
    for idx, (name, role) in enumerate(SPECIALISTS, 1):
        raw = _score(subject, idx)
        severity = SEVERITIES[raw % len(SEVERITIES)]
        confidence = round(0.62 + ((raw % 31) / 100), 2)
        tokens = 4200 + (raw % 9600)
        finding = f"{name} reviewed chain infrastructure operations signal: {subject}. Risk pattern={severity} confidence={confidence}."
        evidence = [
            f"domain=chain infrastructure operations",
            f"subject_hash={hashlib.sha1(subject.encode()).hexdigest()[:10]}",
            f"agent_stage={idx}",
        ]
        recommendation = f"Run {name.lower()} follow-up pass, capture artifacts, then prioritize {severity} items first."
        findings.append(AgentFinding(name, role, severity, confidence, finding, evidence, recommendation, tokens))
    return [f.to_dict() for f in findings]
