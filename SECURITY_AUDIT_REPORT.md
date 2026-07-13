# Security Audit Report — rich
Generated: 2026-07-13

## CI/CD Secret Inventory
- secrets.CODECOV_TOKEN

## Contributor Intelligence
- Abhishek Gupta | 60277134+lgabhishek18@users.noreply.github.com | 2
- shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 1
- GitHub | noreply@github.com | 2

## Branch & Dependency Config
- Dependabot: daily updates for ecosystems: pip (directory: /), github-actions (directory: /)
- Branch protection / staleness: master is protected; 3 stale dependabot/* branches (>30 days); recommendation to delete stale dependabot branches.

## Exposure Summary
- CODECOV_TOKEN: if exfiltrated, could allow unauthorized uploads/association of coverage reports and potentially manipulate CI reporting signals.
