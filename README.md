# ChainOps Autopilot

ChainOps Autopilot is an AI-style infrastructure command center for multi-chain operations teams. It demonstrates how an autonomous agent can monitor RPC health, gas anomalies, validator sync drift, and bridge congestion, then produce a safe remediation trace that reviewers can inspect directly in the browser.

Live demo target: `https://arzillaputriutami-sketch.github.io/agent-chainops/`

## Why this exists

Web3 products frequently depend on multiple fragile infrastructure layers: RPC providers, archive endpoints, bridge relayers, mempool conditions, and validator nodes. A single degraded provider can create user-facing failures even when the underlying chain is healthy.

ChainOps simulates a production SRE workflow:

1. Detect an infrastructure anomaly.
2. Classify root cause and blast radius.
3. Choose a safe automated action.
4. Explain the action in human-readable language.
5. Export proof for audit or reviewer submission.

## Demo features

- Four interactive mission profiles:
  - RPC Storm
  - Gas Surge
  - Node Drift
  - Bridge Queue
- Live topology map with provider and queue states.
- Incident queue with severity labels and mitigation notes.
- Provider latency / risk forecast chart.
- Autonomous remediation trace.
- Terminal-style reasoning transcript.
- Exportable proof report generated fully in the browser.
- No API keys, wallets, private RPC URLs, or backend secrets.

## AI model framing

The public demo uses deterministic browser fixtures so it is safe to host. In a production version, the reasoning layer can be backed by a long-context model such as MiMo or Claude to summarize telemetry, generate incident RCA, and recommend remediation actions.

The browser proof focuses on the workflow and UX:

- Signal collection
- Scenario classification
- Decision trace
- Operator-readable evidence
- Exportable incident report

## Reviewer usage path

1. Open the live demo.
2. Click each mission profile in the left sidebar.
3. Press **Run incident simulation** to cycle scenarios.
4. Inspect the topology, incidents, chart, remediation trace, and terminal transcript.
5. Press **Export proof report** to download a deterministic text report.

## Tech stack

- Static HTML
- Tailwind CDN
- Chart.js
- Vanilla JavaScript
- GitHub Pages deployment

## Safety notes

This repository intentionally contains no private credentials, no wallet material, no server-side code, and no live infrastructure endpoints. All data is synthetic and generated locally in the browser for safe public review.
