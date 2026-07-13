# Security Audit Report — rich
Generated: 2026-07-13

## CI/CD Secret Inventory
- CODECOV_TOKEN

## Contributor Intelligence
- Abhishek Gupta | 60277134+lgabhishek18@users.noreply.github.com | 2
- shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 1
- GitHub | noreply@github.com | 2

## Branch & Dependency Config
### Dependabot
- Ecosystems: pip, github-actions
- Directory: /
- Schedule: daily (for both)

### Branch protection / staleness
Branch Health — shantanuv17/rich
  master         : ✓ protected | last commit: today
  dependabot/*   : 3 stale branches (>30 days, no activity)
  Recommendation : Delete 3 stale dependabot branches
  Open PRs       : 1 (no blocking reviews)

## Exposure Summary
- Highest impact secret identified in workflows: CODECOV_TOKEN (could allow tampering with coverage uploads / reporting).
- No other GitHub Actions secrets were referenced in the workflows inspected.
