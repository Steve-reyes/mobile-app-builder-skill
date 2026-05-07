# Platform Comparison: Mobile App Frameworks

## React Native vs Flutter vs Swift (Native iOS) vs Kotlin (Native Android)

### Framework Comparison

| Factor | React Native | Flutter | Swift (iOS) | Kotlin (Android) |
|---|---|---|---|---|
| **Language** | JavaScript/TypeScript | Dart | Swift | Kotlin |
| **Performance** | Good (JS bridge) | Excellent (Skia engine) | Native | Native |
| **Code Reuse** | ~90% cross-platform | ~95% cross-platform | iOS only | Android only |
| **UI Rendering** | Native components | Custom Skia canvas | UIKit/SwiftUI | Jetpack Compose |
| **Dev Speed** | Fast (hot reload) | Fast (hot reload) | Moderate | Moderate |
| **Startup Time** | Slower | Good | Fastest | Fastest |
| **App Size** | ~7-15MB base | ~15-30MB base | ~5-10MB base | ~5-10MB base |
| **Maturity** | Very mature | Mature | Mature | Mature |
| **Ecosystem** | Large (npm) | Growing (pub.dev) | Apple ecosystem | Google ecosystem |
| **Community** | Very large | Large | Large | Large |
| **Hiring** | Easy to find | Growing | Moderate | Moderate |
| **Best For** | MVPs, CRUD apps | Beautiful UI, cross-platform | iOS-first apps | Android-first apps |

### Decision Guide

| Situation | Recommendation |
|---|---|
| Need iOS + Android fast, simple UI | React Native |
| Need iOS + Android with custom UI/animation | Flutter |
| iOS-only app, Apple ecosystem deep integration | Swift |
| Android-only app, Google ecosystem deep integration | Kotlin |
| Heavy camera/AR/Bluetooth usage | Swift or Kotlin (native) |
| Tight budget, need both platforms | Flutter |

### Cost Comparison (MVP)

| Framework | Dev Time | Dev Cost (Junior) | Dev Cost (Senior) |
|---|---|---|---|
| React Native | 2-4 months | $8K-16K | $20K-40K |
| Flutter | 2-4 months | $8K-16K | $20K-40K |
| Swift (iOS only) | 1-2 months | $5K-10K | $12K-25K |
| Kotlin (Android only) | 1-2 months | $5K-10K | $12K-25K |
| Both Native (Swift + Kotlin) | 3-6 months | $15K-30K | $30K-60K |
