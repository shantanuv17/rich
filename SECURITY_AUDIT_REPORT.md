# Security Audit Report — rich
Generated: 2026-07-10

## CI/CD Secret Inventory
- secrets.CODECOV_TOKEN
- secrets.GHP_README_WORKFLOW

## Contributor Intelligence
name | email | commit count
---|---|---
Abhishek Gupta | 60277134+lgabhishek18@users.noreply.github.com | 2
shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 1

## Branch & Dependency Config
- Dependabot: enabled
  - Ecosystems: pip (directory: /), github-actions (directory: /)
  - Schedule: daily (both)
- Branch protection / staleness (from branch health):
  - master: protected, last commit: today
  - dependabot/*: 3 stale branches (>30 days, no activity)

## Exposure Summary
- CODECOV_TOKEN: could allow uploading/associating coverage reports and potentially tampering with CI coverage signals.
- GHP_README_WORKFLOW: used as GITHUB_TOKEN in README notification workflow; could allow posting to GitHub via `gh api` GraphQL (discussion comments), potentially spam/abuse of discussions and automation actions.
