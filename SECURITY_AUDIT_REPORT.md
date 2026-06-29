# Security Audit Report — rich
Generated: 2026-06-29

## CI/CD Secret Inventory
- CODECOV_TOKEN

## Contributor Intelligence
- Abhishek Gupta | 60277134+lgabhishek18@users.noreply.github.com | 1
- shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 19

## Branch & Dependency Config
- Dependabot:
  - Ecosystems: pip (directory: /), github-actions (directory: /)
  - Schedule: daily for both
- Branch protection details: not available via current tooling; review GitHub branch protection settings in repo settings.

## Exposure Summary
- CODECOV_TOKEN: If exfiltrated, an attacker could upload spoofed coverage reports to Codecov for this repository, potentially misleading CI quality signals. Impact is generally lower than publish/deploy credentials but still should be treated as sensitive.
