# Security Audit Report — rich
Generated: 2026-07-08

## CI/CD Secret Inventory
- CODECOV_TOKEN

## Contributor Intelligence
- Abhishek Gupta | 60277134+lgabhishek18@users.noreply.github.com | 13
- shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 7

## Branch & Dependency Config
- Dependabot: interval=daily; ecosystems=pip (/) and github-actions (/)
- Branch protection: `master` is protected (per branch health report)
- Branch hygiene: 3 stale `dependabot/*` branches (>30 days) recommended for deletion

## Exposure Summary
- Highest impact secret: `CODECOV_TOKEN` (could allow unauthorized coverage uploads / CI signal manipulation if compromised).
- No other workflow secrets were referenced in the inspected workflows.
