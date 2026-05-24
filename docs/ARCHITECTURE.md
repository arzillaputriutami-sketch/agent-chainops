# ChainOps Autopilot Architecture

## Purpose

SRE-grade agent cockpit for RPC reliability, sync stalls, peer health, and automated runbooks.

## Runtime loop

1. **Observe** — collect domain signals: rpc_p95_ms, missed_blocks, peer_churn, disk_growth_gb, region_error_rate.
2. **Orient** — map the active scenario to specialist agent responsibilities.
3. **Decide** — score severity, confidence, and operator urgency.
4. **Act** — emit next actions that a human operator can verify.
5. **Reflect** — attach trace IDs and deterministic evidence for review.

## Components

- `backend/swarm.py` — pure Python reasoning core, safe for CI and static demos.
- `backend/app.py` — FastAPI wrapper for product integration.
- `cli.py` — terminal demo path for reviewers.
- `index.html` — front-facing dashboard surface.

## Agent responsibilities

- `RPC Health Watcher`: owns one part of the analysis loop.
- `Peer Quality Analyst`: owns one part of the analysis loop.
- `Sync Stall Diagnoser`: owns one part of the analysis loop.
- `Cost-Aware Capacity Planner`: owns one part of the analysis loop.
- `Runbook Commander`: owns one part of the analysis loop.

## Production extension points

- Replace deterministic signals with live connectors.
- Persist reports in Postgres or SQLite.
- Add auth and organization workspaces.
- Add export hooks for Slack, Discord, Telegram, or email.
