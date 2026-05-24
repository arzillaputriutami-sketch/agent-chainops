# ChainOps Autopilot Architecture

## Goal
Create a polished proof-of-usage demo that makes an infrastructure agent feel real to a reviewer without requiring backend services or secrets.

## Architecture

- `index.html`
  - UI shell, scenario navigation, metrics, charts, incident queue, terminal transcript, export action.
- `README.md`
  - Reviewer-facing explanation of problem, UX, and demo flow.
- Browser-only runtime
  - Deterministic scenario data embedded in the page.
  - JavaScript renders scenario changes and builds the proof report.
- Chart.js
  - Used for visualizing synthetic latency/risk telemetry.
- Tailwind CDN
  - Provides utility styling without a build step.

## Interaction model

1. User opens the page.
2. User selects a mission profile.
3. The page loads the matching incident dataset.
4. The operator sees:
   - severity labels
   - metric counters
   - topology map state
   - remediation trace
   - terminal log
5. The export button generates a plain-text proof report.

## Design principles

- High contrast, premium dark UI.
- Clear separation of signal, analysis, and action.
- Deterministic behavior for reproducibility.
- No dependency on backend APIs.
- No sensitive data exposure.

## Submission value

This project demonstrates more than a pretty screen. It shows a complete narrative:

- monitoring
- diagnosis
- response
- verification
- evidence export

That makes it suitable for incentive programs that want proof of actual product behavior instead of empty screenshots.
