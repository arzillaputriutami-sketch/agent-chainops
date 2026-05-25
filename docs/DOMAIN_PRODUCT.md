# Agent ChainOps — Domain Product Layer

Autonomous chain operations cockpit for RPC reliability, sync stalls, peer health, and automated runbooks.

## Live Reviewer Endpoints

- `GET /domain/signals` — inspect supported domain signals and actions
- `POST /domain/analyze` — submit scenario + signals, receive risk score, findings, runbook, trace id
- `GET /domain/demo` — four deterministic demo reports
- `POST /agent-run` — MiMo multi-specialist pipeline proof

## Signals

- `rpc_p95_ms`
- `sync_lag_blocks`
- `peer_count`
- `missed_slots`
- `disk_growth_gb`
- `error_rate`

## Operator Actions

- quarantine weak RPC endpoint
- rotate relayer queue
- restart indexer with bounded backoff
- open validator incident brief
- promote healthy peer set
