# Security Audit Report — rich
Generated: 2026-06-29

## CI/CD Secret Inventory
- CODECOV_TOKEN

## Contributor Intelligence
- Abhishek Gupta | 60277134+lgabhishek18@users.noreply.github.com | 1
- shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 1

## Branch & Dependency Config
- Dependabot: interval=daily; ecosystems=pip (/) and github-actions (/)
- Branch health: master is protected; 3 stale dependabot/* branches (>30 days); 1 open PR

## Exposure Summary
Most damaging exposure would be CODECOV_TOKEN (could allow tampering with coverage uploads / CI signal integrity depending on Codecov project settings).