# Security Audit Report — rich
Generated: 2026-07-13

## CI/CD Secret Inventory
- CODECOV_TOKEN

## Contributor Intelligence
- Abhishek Gupta | 60277134+lgabhishek18@users.noreply.github.com | 2
- shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 2
- GitHub | noreply@github.com | 2

## Branch & Dependency Config
- Dependabot: interval=daily; ecosystems=pip ("/") and github-actions ("/")
- Branch protection: master is protected (per branch health)
- Branch health: 3 stale dependabot/* branches (>30 days), recommendation to delete; open PRs: 1

## Exposure Summary
- Highest impact secret: CODECOV_TOKEN (could enable an attacker to upload/overwrite coverage reports; may be used to access Codecov project context depending on org settings).
