# Yojana Sahayak Frontend Expansion Plan

**Date:** 2026-10-31

This plan addresses the "ADDITIONAL FEATURES PROMPT" to expand the frontend of Yojana Sahayak. **All work will be frontend only, mock-first.**

## Task Order

### 1. Voice Assistant Core (Section 3)
*   **Goal:** Implement the hands-free voice mode state machine, speech-to-text (STT), text-to-speech (TTS), and review-before-send flow.
*   **Files Touched:**
    *   `apps/web/src/pages/VoiceAssistant.tsx` (New main view)
    *   `apps/web/src/components/voice/OrbVisual.tsx` (Animated visual)
    *   `apps/web/src/lib/voice/machine.ts` (State machine logic)
    *   `apps/web/src/lib/voice/speech.ts` (STT/TTS wrappers)
    *   `apps/web/src/locales/en.json`, `apps/web/src/locales/hi.json` (i18n strings)
    *   `apps/web/src/App.tsx` (Add routing)
    *   `apps/web/src/components/layout/BottomNav.tsx` (Add navigation item)

### 2. Voice Extras (Section 3)
*   **Goal:** Add barge-in support, voice availability notices, settings, and the voice-driven questionnaire fallback.
*   **Files Touched:**
    *   `apps/web/src/lib/voice/machine.ts` (Barge-in logic)
    *   `apps/web/src/components/voice/VoiceSettings.tsx`
    *   `apps/web/src/components/voice/VoiceQuestionnaire.tsx`
    *   `apps/web/src/pages/VoiceAssistant.tsx` (Integrate extras)

### 3. What's New Feed + Alerts (Section 4)
*   **Goal:** Implement the "Recently added" feed and notification center, reading only verified mock data.
*   **Files Touched:**
    *   `apps/web/src/pages/WhatsNew.tsx` (New feed view)
    *   `apps/web/src/components/feed/FeedItem.tsx`
    *   `apps/web/src/components/notifications/NotificationCenter.tsx`
    *   `apps/web/src/lib/api/adapters/mock/feed.ts` (Mock endpoints)
    *   `apps/web/src/lib/db/indexeddb.ts` (Add notifications store)

### 4. Map: Where to Apply (A1)
*   **Goal:** Implement the interactive Leaflet map for office discovery.
*   **Files Touched:**
    *   `apps/web/src/pages/OfficesMap.tsx`
    *   `apps/web/src/components/map/LeafletWrapper.tsx`
    *   `apps/web/src/lib/api/adapters/mock/offices.ts`
    *   `apps/web/package.json` (Add `leaflet` and `react-leaflet`)

### 5. Compare + Life Events (A2, A3)
*   **Goal:** Implement side-by-side scheme comparison and the life-event curated discovery flows.
*   **Files Touched:**
    *   `apps/web/src/pages/Compare.tsx`
    *   `apps/web/src/pages/LifeEvents.tsx`
    *   `apps/web/src/components/compare/CompareTable.tsx`
    *   `apps/web/src/lib/api/adapters/mock/life-events.ts`

### 6. Tracker + Document Readiness + Deadlines (A4, A5, A6)
*   **Goal:** Build the personal tracker, aggregated document checklist, and verified deadlines calendar.
*   **Files Touched:**
    *   `apps/web/src/pages/ApplicationTracker.tsx`
    *   `apps/web/src/pages/DocumentReadiness.tsx`
    *   `apps/web/src/pages/Deadlines.tsx`
    *   `apps/web/src/lib/db/indexeddb.ts` (Add tracker store)
    *   `apps/web/src/lib/calendar/ics.ts` (ICS generation utility)

### 7. Household Profiles + Volunteer Mode (A7, A8)
*   **Goal:** Implement local profile switching and the session-only volunteer mode.
*   **Files Touched:**
    *   `apps/web/src/lib/store/profile.ts` (Zustand store updates)
    *   `apps/web/src/components/profile/ProfileSwitcher.tsx`
    *   `apps/web/src/components/layout/VolunteerBanner.tsx`

### 8. Share/QR/Print + Accessibility + Feedback (A9, A10, A11)
*   **Goal:** Implement sharing controls, accessibility overrides, and feedback buttons.
*   **Files Touched:**
    *   `apps/web/src/components/shared/ShareControls.tsx` (QR generation, Web Share API)
    *   `apps/web/src/pages/Settings.tsx` (Accessibility toggles)
    *   `apps/web/src/components/shared/FeedbackWidget.tsx`
    *   `apps/web/src/index.css` (Print stylesheet additions, High contrast variables)

### 9. Tier B Previews + Roadmap + Languages (Tier B)
*   **Goal:** Add disabled states for future channels (WhatsApp, Push) and document language addition.
*   **Files Touched:**
    *   `apps/web/src/pages/Roadmap.tsx`
    *   `apps/web/src/components/preview/WhatsAppPreview.tsx`
    *   `docs/ADDING_A_LANGUAGE.md` (New documentation file)

### 10. Integration Docs, Status Report, Regression
*   **Goal:** Finalize documentation and verify all tests pass.
*   **Files Touched:**
    *   `docs/FRONTEND_INTEGRATION.md` (Update API proposals)
    *   `docs/FRONTEND_STATUS.md` (Update completion status)
