# Security Audit Report — rich
Generated: 2026-07-07

## CI/CD Secret Inventory
- CODECOV_TOKEN

## Contributor Intelligence
(Last 20 commits)
- Abhishek Gupta | 60277134+lgabhishek18@users.noreply.github.com | 2
- shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 1

## Branch & Dependency Config
- Dependabot: enabled
  - Ecosystems: pip (/) daily; github-actions (/) daily
- Branch protection: master is protected (per branch health scan)
- Branch hygiene: 3 stale dependabot/* branches recommended for deletion

## Exposure Summary
- Highest-impact secret observed: CODECOV_TOKEN. If exfiltrated, it could allow an attacker to upload forged coverage reports or interact with Codecov for this repo.
- No other GitHub Actions secrets were referenced in the workflow files reviewed.
