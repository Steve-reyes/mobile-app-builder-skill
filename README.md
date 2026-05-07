# Mobile App Builder Skill

**Analyze any mobile app or app idea → complete build plan with full mobile infra design.**

## What It Does

Given a competitor app name/URL or app idea, this skill:
1. **Researches** the app (App Store/Play Store listing, features, platform, pricing, ratings)
2. **Analyzes feasibility** — what's standard mobile dev vs what's the moat
3. **Generates a complete build plan** with:
   - Architecture overview (mobile + backend)
   - Platform decision (React Native vs Flutter vs Swift vs Kotlin) with justification
   - Full directory structure
   - Database schema (PostgreSQL / Firebase)
   - REST API endpoints
   - UI/UX key screens list
   - Third-party integrations (Firebase, Stripe, Maps, etc.)
   - Tech stack decisions with rationale
   - Realistic MVP build timeline
   - Cost estimates (one-time + monthly)
   - App Store submission checklist
   - Launch & marketing strategy
   - Future scaling roadmap

## How to Use

> "analyze app [name]"
> "build plan for app [url]"
> "clone app [name]"
> "mobile app idea [description]"
> "deconstruct app [name]"

The skill produces a markdown file saved to `steve_app_ideas/` and auto-pushed to the `app_ideas` GitHub repo.

## Output Format

Every plan follows this structure:

```
1. What [App] Is — Description, user flows, target audience
2. What Makes It Hard — Feature difficulty matrix, true moats
3. MVP That CAN Be Built — Honest scope, what's excluded
4. Complete Infra Design — Architecture, platform decision, directory, DB, API, UI screens, integrations, stack, timeline, costs, app store, launch
```

## Resources

| File | Purpose |
|---|---|
| `SKILL.md` | Main skill instructions and workflow |
| `scripts/research_app.py` | Automated app research |
| `scripts/generate_plan.py` | Validate research and output plan path |
| `references/build-plan-template.md` | Full template for mobile app build plans |
| `references/platform-comparison.md` | React Native vs Flutter vs Swift vs Kotlin deep comparison |

## Requirements

- Python 3.12+
- web_search and web_fetch tools available
- Git configured with GitHub remote
- `steve_app_ideas/` directory with post-commit hook for auto-push
- Interest in mobile app development

## Installation

```bash
openclaw skill install mobile-app-builder
```

Or install from the packaged skill file:

```bash
openclaw skill install mobile-app-builder.skill
```
