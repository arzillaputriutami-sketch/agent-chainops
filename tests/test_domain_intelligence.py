from backend.domain.intelligence import analyze_domain, batch_domain_report, SIGNALS


def test_domain_report_schema():
    out = analyze_domain('RPC p95 spikes while indexer lag grows').to_dict()
    assert out["product"] == 'Agent ChainOps'
    assert out["domain"] == 'chain operations / node reliability'
    assert 0 <= out["risk_score"] <= 100
    assert len(out["findings"]) == len(SIGNALS)
    assert out["token_budget"]["total_estimated_tokens"] > 25000


def test_domain_signal_override_changes_trace():
    a = analyze_domain('RPC p95 spikes while indexer lag grows').to_dict()
    b = analyze_domain('RPC p95 spikes while indexer lag grows', {SIGNALS[0]: 99}).to_dict()
    assert a["trace_id"] != b["trace_id"]
    assert b["findings"][0]["value"] == 99.0


def test_batch_domain_report_covers_scenarios():
    reports = batch_domain_report()
    assert len(reports) >= 4
    assert all("runbook" in r for r in reports)
