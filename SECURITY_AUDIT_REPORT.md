# Security Audit Report — rich
Generated: 2026-07-10

## CI/CD Secret Inventory
- CODECOV_TOKEN
- GHP_README_WORKFLOW

## Contributor Intelligence
shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 2
Abhishek Gupta | 60277134+lgabhishek18@users.noreply.github.com | 2
GitHub | noreply@github.com | 2

## Branch & Dependency Config
- Dependabot
  - Ecosystems: pip (/) daily; github-actions (/) daily
- Branch protection / staleness
  - master: protected, last commit today
  - dependabot/*: 3 stale branches (>30 days, no activity)

## Exposure Summary
- CODECOV_TOKEN: could allow uploading / spoofing coverage reports to Codecov; moderate impact on CI integrity.
- GHP_README_WORKFLOW: GitHub token used in workflow to post a discussion comment; if scoped broadly could allow repo/discussion write actions; potentially higher impact depending on permissions.
