---
name: mobile-app-builder
description: |
  Analyze any mobile app (iOS/Android) or app idea and produce a complete build plan with full mobile infra design, platform architecture, and launch strategy.
  Triggers: "analyze app [name]", "build plan for app [url]", "clone app [name]", "what would it take to build [app like x]", "deconstruct app [name]", "reverse engineer [app]", "mobile app idea [description]".
  Use when the user wants to understand a competitor mobile app, estimate build effort, or get a ready-to-execute project plan with mobile architecture, UI/UX design specs, backend infra, app store strategy, timeline, and costs.
---

# Mobile App Builder

Given a competitor app URL/app name or app idea, research it and produce a structured build plan saved to `mobile_app_ideas/` folder and auto-pushed to the `mobile-app-ideas` GitHub repo.

## Workflow

### 1. Research the App

Use `web_search` and `web_fetch` to gather:

- App description (App Store / Play Store listing, tagline, category)
- Core features & user flows
- Platform (iOS native, Android native, React Native, Flutter, etc.)
- Pricing model (free, freemium, subscription, IAP, ads)
- Target audience
- Ratings, reviews, download estimates
- Competitors in the space
- Tech stack hints (public info, job postings, engineering blogs)

### 2. Feasibility Breakdown

Classify each component into one of three buckets:

| Difficulty | Label | Criteria |
|---|---|---|
| 🟢 Easy | Standard mobile dev | Standard screens, CRUD, auth, push notifications |
| 🟡 Medium | Complex mobile features | Maps, camera/AR, real-time chat, offline sync, payments |
| 🔴 Hard | The moat | Proprietary algorithms, hardware integration, network effects, regulatory (health/fintech), massive content/library |

### 3. Generate the Build Plan

Create a markdown file at: `mobile_app_ideas/<app-name>.md`

Structure (follow `references/build-plan-template.md`):

```
# <App Name> Analysis & Build Plan

## 1. What <App Name> Is
## 2. What Makes It Hard (moats)
## 3. MVP That CAN Be Built
## 4. Complete Project Infra Design
### Architecture Overview
### Platform Decision (Native vs Cross-Platform)
### Directory Structure (Mobile + Backend)
### Database Schema (PostgreSQL / Firebase)
### API Endpoints
### Product Requirements Document (PRD)
### Competitive Landscape Matrix
### UI/UX Key Screens
### Third-Party Integrations
### AI Agent Design (if applicable)
### SEO & Content Strategy
### Growth & Viral Loops
### Revenue Model & Unit Economics
### Tech Stack Summary
### Estimated MVP Build Time
### Cost Estimates (Monthly + One-Time)
### App Store Submission Checklist
### Launch & Marketing Strategy
### Future Phases
```

### 4. Save & Push

```bash
cd /root/.openclaw/agents/researcher/workspace/mobile_app_ideas
git add <filename>.md
git commit -m "Add build plan: <App Name>"
```

Auto-push is handled by post-commit hook.

## Execution Rules

- Always check App Store + Play Store listings first for description, screenshots, ratings
- Platform decision must be justified: React Native vs Flutter vs Swift vs Kotlin
- Include UI/UX key screen list (login, home, feed, profile, etc.)
- Always include App Store submission checklist (Apple guidelines, TestFlight, review times)
- Include launch strategy (ASO, social, paid acquisition, influencer)
- Database schema must include core entities with proper relationships
- API endpoints must follow REST conventions
- After writing the file, always commit and verify the push

## Resources

### scripts/
- `research_app.py` — Research script for App Store / Play Store data
- `generate_plan.py` — Validate research and output plan path

### references/
- `build-plan-template.md` — Full template for every mobile app build plan
- `platform-comparison.md` — React Native vs Flutter vs Swift vs Kotlin comparison
- `prd-template.md` — Product Requirements Document template
- `competitive-landscape.md` — Feature comparison across competitors
- `seo-content-strategy.md` — Keyword clusters, content funnel, distribution
- `growth-loops.md` — Viral mechanics, acquisition channels, referral design
- `revenue-model.md` — Pricing tiers, CAC/LTV, break-even analysis
