# {{APP_NAME}} Analysis & Build Plan

> **Date:** {{DATE}}
> **Source:** {{APP_STORE_URL}} / {{PLAY_STORE_URL}}
> **Status:** Competitor analysis → MVP build scope

---

## 1. What {{APP_NAME}} Is

Brief description: category, core value prop, top features, platform(s), pricing model, ratings/reviews, estimated downloads.

### Key User Flows
1. **Flow 1** — Onboarding → core action
2. **Flow 2** — Secondary action path
3. **Flow 3** — Monetization flow

### Target Audience
Demographics, use case, pain points solved.

---

## 2. What Makes It Hard

| Component | Difficulty | Why |
|---|---|---|
| {{Feature 1}} | 🟢/🟡/🔴 | Reason |
| {{Feature 2}} | 🟢/🟡/🔴 | Reason |
| {{Feature 3}} | 🟢/🟡/🔴 | Reason |

### The Moats
- Proprietary data/algorithm
- Network effects / community
- Hardware integration
- Regulatory (health, fintech, legal)
- Brand trust / content library

---

## 3. MVP That CAN Be Built

### MVP Features
1. **Feature 1** — Description
2. **Feature 2** — Description
3. **Feature 3** — Description

### What We DON'T Build (MVP)
- Items explicitly excluded

---

## 4. Complete Project Infra Design

### Architecture Overview
```
┌─────────────────────────────────────┐
│         Mobile App ({{PLATFORM}})      │
│   - {{SCREEN_LIST}}                  │
└──────────────┬──────────────────────┘
               │ REST/WebSocket
┌──────────────▼──────────────────────┐
│           Backend API ({{STACK}})      │
│      {{HOSTING}}                      │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│          Database ({{DB}})             │
│   - {{TABLE_LIST}}                   │
└─────────────────────────────────────┘
               │
┌──────────────▼──────────────────────┐
│    Third-Party Services             │
│   - Auth, Payments, Push, Analytics │
└─────────────────────────────────────┘
```

### Platform Decision

| Factor | {{OPTION 1}} | {{OPTION 2}} | {{OPTION 3}} |
|---|---|---|---|
| Dev Speed | | | |
| Performance | | | |
| Cost | | | |
| Team Availability | | | |
| Recommendation | | | |

**Verdict:** Why we chose {{PLATFORM}}.

### Directory Structure
```
{{APP_NAME}}/
├── mobile/                    # Mobile app codebase
│   ├── app/                   # Main app code
│   ├── components/            # Reusable UI components
│   ├── screens/               # Screen-level components
│   ├── services/              # API clients, auth, push
│   ├── store/                 # State management
│   ├── utils/                 # Helpers
│   ├── assets/                # Images, fonts, icons
│   └── pubspec.yaml / package.json
│
├── backend/                   # Server (if applicable)
│   ├── app/
│   ├── routers/
│   ├── services/
│   └── requirements.txt
│
├── shared/                    # Shared types/schemas
├── docker-compose.yml
└── .env.example
```

### Database Schema

```sql
-- Core tables
CREATE TABLE users ( ... );
CREATE TABLE ... ( ... );
```

### API Endpoints

```
POST   /api/auth/register
POST   /api/auth/login
GET    /api/resource
POST   /api/resource
```

### UI/UX Key Screens

| Screen | Description | Key Elements |
|---|---|---|
| Splash/Onboarding | | |
| Auth (Login/Signup) | | |
| Home/Feed | | |
| Detail | | |
| Profile | | |
| Settings | | |

### Third-Party Integrations

| Service | Purpose | Cost |
|---|---|---|
| Firebase | Auth, Push, Analytics | Free tier |
| Stripe/RevenueCat | Payments | % per transaction |
| Mapbox/Google Maps | Maps | Usage-based |
| Sentry | Error tracking | Free tier |
| Amplitude/Mixpanel | Analytics | Free tier |

### Tech Stack Summary

| Layer | Choice | Reason |
|---|---|---|
| Mobile Framework | Flutter / React Native / Swift / Kotlin | |
| State Management | Riverpod / Redux / Provider | |
| Backend | FastAPI / Node / Firebase | |
| Database | PostgreSQL / Firebase Firestore | |
| Auth | Firebase Auth / Supabase | |
| Payments | RevenueCat / Stripe | |
| Push | Firebase Cloud Messaging | |
| Hosting | Railway / Vercel / Firebase | |
| CI/CD | GitHub Actions + Codemagic | |

### Estimated MVP Build Time

| Phase | Time | Deliverable |
|---|---|---|
| Design (UI/UX) | X days | Figma screens |
| Auth & Onboarding | X days | |
| Core Feature 1 | X days | |
| Core Feature 2 | X days | |
| Backend + API | X days | |
| Testing + Polish | X days | |
| App Store Prep | X days | |
| **Total** | **X days** | **MVP** |

### Cost Estimates

| Item | One-Time | Monthly |
|---|---|---|
| Apple Developer Account | $99/yr | - |
| Google Play Account | $25 (one-time) | - |
| Backend Hosting | - | $X |
| Database | - | $X |
| Third-Party APIs | - | $X |
| App Design (if outsourced) | $X | - |
| **Total** | **$X** | **$X/mo** |

### App Store Submission Checklist

- [ ] Apple Developer Program enrollment ($99/yr)
- [ ] App icons all sizes
- [ ] Screenshots (6.7", 6.5", 5.5", iPad)
- [ ] App description + keywords (ASO)
- [ ] Privacy policy URL
- [ ] Terms of service
- [ ] TestFlight internal + external testers
- [ ] No crashes on latest iOS/Android
- [ ] Offline handling tested
- [ ] Push notification permissions
- [ ] Review guidelines compliance

### Launch & Marketing Strategy

- App Store Optimization (keywords, description, screenshots)
- Product Hunt launch
- Social media (TikTok demo, Twitter/X thread)
- Influencer partnerships (micro)
- Paid acquisition (Apple Search Ads, Google UAC)
- Content marketing (blog, tutorial videos)
- Community (Reddit, Discord, Slack groups)

### Future Phases

**Phase 2 — Description**

**Phase 3 — Description**

---

*Last updated: {{DATE}}*
