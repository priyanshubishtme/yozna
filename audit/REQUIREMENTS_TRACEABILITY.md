# Requirements Traceability

This document maps the requirements specified in the blueprint to the current implementation.

| Requirement ID | Feature Name | Expected Behavior | Implementation Status |
| --- | --- | --- | --- |
| FR-01 | Bilingual chat | Ask in Hindi or English; answer in the user's language. | PARTIALLY IMPLEMENTED (Endpoint exists but RAG logic is mock/minimal) |
| FR-02 | Grounded answers | Factual content is based on retrieved verified documents. | NOT IMPLEMENTED |
| FR-03 | Citation validation | Every factual sentence has valid backend-resolved citations or is removed/refused. | NOT IMPLEMENTED |
| FR-04 | Evidence refusal | Weak or absent evidence returns an honest insufficient-information response. | NOT IMPLEMENTED |
| FR-05 | PDF evidence viewer | Citation opens the exact source page and highlights stored coordinates. | FRONTEND ONLY (Mock placeholder component) |
| FR-06 | Scheme registry | Store schemes, source records, authoritative documents and versions. | PARTIALLY IMPLEMENTED (Database models exist, but no real integration/logic) |
| FR-07 | Full discovery system | Discover permitted new/updated scheme resources through source adapters. | NOT IMPLEMENTED |
| FR-08 | Source scheduling | APScheduler runs configured source checks and supports manual runs. | PARTIALLY IMPLEMENTED (A dummy job exists) |
| FR-09 | Fingerprint/change detection | Detect new, unchanged, changed, duplicate and unavailable resources. | NOT IMPLEMENTED |
| FR-10 | Review queue | New and changed resources enter Pending Review; they are not live until approved. | NOT IMPLEMENTED |
| FR-11 | Rule invalidation | Changed source dependencies flag associated rules for re-review. | NOT IMPLEMENTED |
| FR-12 | Eligibility questionnaire | Guided profile questions; unknown/Not sure is supported. | NOT IMPLEMENTED |
| FR-13 | Deterministic eligibility | Only approved rules evaluated by Python. | PARTIALLY IMPLEMENTED (Basic skeleton exists, not hooked to data) |
| FR-14 | Four outcomes | Eligible, Likely Eligible, Need More Information, Not Eligible. | PARTIALLY IMPLEMENTED (In python class, not exposed) |
| FR-15 | Scheme ranking | Explainable ranking by status, verified application timing, user relevance and documented benefits. | NOT IMPLEMENTED |
| FR-16 | Scheme discovery | Search, categories, filters and scheme details. | NOT IMPLEMENTED |
| FR-17 | My Schemes | Save schemes and access them offline. | NOT IMPLEMENTED |
| FR-18 | Document checklist | Track user-side collection of required documents; checklist is not government verification. | NOT IMPLEMENTED |
| FR-19 | PWA | Installable app, manifest, service worker, offline shell and update UX. | NOT IMPLEMENTED |
| FR-20 | Voice | Browser-native speech input/output with feature detection and text fallback. | NOT IMPLEMENTED |
| FR-21 | Admin portal | Source registry, jobs, candidates, documents, versions, rule reviews, ingestion and audit logs. | NOT IMPLEMENTED |
| FR-22 | History | Retain discovery and document lifecycle history. | NOT IMPLEMENTED |
| FR-23 | Email reminders | Opt-in, verified email reminders for saved schemes/deadlines where dates are verified. | NOT IMPLEMENTED |
| FR-24 | Analytics | Privacy-preserving aggregate operational and product metrics. | NOT IMPLEMENTED |
| FR-25 | 3D animated SaaS UI | Premium public landing page and coherent animated application UI. | FRONTEND ONLY (Basic tailwind, no 3D or GSAP) |
| FR-26 | Settings and privacy | Language, theme, profile controls, consent and data deletion. | NOT IMPLEMENTED |