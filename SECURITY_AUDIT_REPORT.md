# Security Audit Report — rich
Generated: 2026-05-13

## CI/CD Secret Inventory
- CODECOV_TOKEN

## Contributor Intelligence
name | email | commit count (last 20 commits)
- shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 20

## Branch & Dependency Config
### Dependabot
- Ecosystems monitored: pip, github-actions
- Schedule: daily (both)
- Directory: / (both)

### Branch protection / branch health
- master: protected; last commit: today
- 3 stale dependabot/* branches (>30 days)
- Open PRs: 1 (no blocking reviews)

## Exposure Summary
- `CODECOV_TOKEN`: If exfiltrated, could allow an attacker to upload/overwrite coverage reports (integrity risk for CI reporting) and potentially access org/project metrics depending on Codecov configuration. Rotate if suspected compromised.
