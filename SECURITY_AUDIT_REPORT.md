# Security Audit Report — rich
Generated: 2026-07-13

## CI/CD Secret Inventory
- CODECOV_TOKEN

## Contributor Intelligence
- shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 2
- Abhishek Gupta | 60277134+lgabhishek18@users.noreply.github.com | 2
- GitHub | noreply@github.com | 0

## Branch & Dependency Config
### Dependabot
- Ecosystems: pip, github-actions
- Directory: /
- Schedule: daily (for both)

### Branch protection (observed via branch listing metadata)
- main: protected=false
- master: protected=false

## Exposure Summary
- Highest impact: CODECOV_TOKEN (could allow an attacker to upload/poison coverage reports, potentially affecting CI signal integrity and, depending on Codecov project settings, access to coverage data and repository metadata).
