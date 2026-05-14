# Security Audit Report — rich
Generated: 2026-05-14

## CI/CD Secret Inventory
- `CODECOV_TOKEN`

## Contributor Intelligence
name | email | commit count (last 20 commits)
--- | --- | ---
shantanuv17 | 48430514+shantanuv17@users.noreply.github.com | 20

## Branch & Dependency Config
### Dependabot
- Ecosystems monitored: `pip`, `github-actions`
- Directory: `/`
- Schedule: daily for both ecosystems

### Branch / Repo config (from repository metadata)
- Default branch: `master`
- Repo: fork of `Textualize/rich`
- Branch protection details: not available via current API calls in this session

## Exposure Summary
- `CODECOV_TOKEN`: if exfiltrated, could allow uploading/overwriting coverage reports for this project in Codecov, potentially masking CI coverage signals. Impact depends on Codecov org/project permissions; generally medium risk versus publishing keys.
