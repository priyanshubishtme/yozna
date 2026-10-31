# Yojana Sahayak Build Verification Report

**Date:** 2026-10-31

## 1. Executive Verdict
The repository contains 0% of the completed end-to-end functionality required by `BLUEPRINT_V2.md`. Overall completion is approximately **5%** (Formula: (0 PASS + 5 PARTIAL + 5 STUB + 16 MISSING) / 26 Functional Requirements). The codebase consists merely of initialized React and FastAPI boilerplates, with simple dummy endpoints and components to mock basic shapes (like a mock chat interface and fake PDF viewer). The single biggest risk is that **no actual data pipeline, document scraping, RAG integration, or PWA capabilities have been implemented.**

## 2. Scoreboard

| Category | PASS | PARTIAL | STUB | MISSING | BROKEN | VIOLATION | BLOCKED | UNVERIFIED |
|---|---|---|---|---|---|---|---|---|
| **FRs (26)** | 0 | 4 | 5 | 17 | 0 | 0 | 0 | 0 |
| **NFRs** | 0 | 2 | 2 | 10 | 0 | 0 | 0 | 0 |
| **Integrity Rules (10)** | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 |
| **Phase Gates (0-14)** | 1 | 0 | 1 | 13 | 0 | 0 | 0 | 0 |
| **DoD** | 0 | 0 | 1 | 17 | 0 | 0 | 0 | 0 |

## 3. Per-File Verification

| Path | Lines | Status | Purpose actually implemented | Blueprint ref | Evidence | Problems |
|---|---|---|---|---|---|---|
| `apps/web/src/App.tsx` | 16 | STUB | Basic React Router | §11.4 | `cat apps/web/src/App.tsx` shows only `/` and `/app/chat` | Missing all other routes. |
| `apps/web/src/components/ChatInterface.tsx` | 114 | PARTIAL | UI for chat streaming | §11.5 | `fetch('/api/v1/chat')` | Only talks to mock endpoint. |
| `apps/web/src/components/PDFViewer.tsx` | 21 | STUB | Mock PDF Viewer | §11.6 | Hardcoded `<div class="absolute ... bg-yellow-300">` | No actual PDF.js implementation. |
| `backend/app/main.py` | 10 | PARTIAL | FastAPI app | §2.3 | `uvicorn app.main:app` runs | Missing CORS, error handling, other routers. |
| `backend/app/api/v1/chat.py` | 33 | STUB | Dummy chat streaming | §12.1 | `yield "data: [DONE]"` | Hardcoded "Thinking about {query}" responses when no key provided. |
| `backend/app/db/models.py` | 29 | STUB | SQLAlchemy models | §13.1 | Class definitions exist | Unused in the app. Misses most required tables. |
| `backend/app/eligibility/evaluator.py` | 25 | STUB | Python evaluator | §13 | Returns hardcoded strings | Not connected to any API or database rules. |
| `backend/app/ingest/extract.py` | 28 | STUB | PyMuPDF extraction | §7 | `extract_pdf_text_and_boxes` defined | Dead code, not integrated into any pipeline. |
| `backend/app/scheduler/run.py` | 15 | STUB | APScheduler setup | §6.1 | Prints "Test job executed" | Dummy job only. |
| `backend/app/llm/providers.py` | 28 | PARTIAL | AsyncOpenAI wrapper | §9.4 | Reads `GROQ_API_KEY` | Bypassed if key missing. |

## 4. Requirement Audits

### Functional Requirements (FR)
* **FR-01 (Bilingual chat):** STUB. The endpoint exists but returns mocked English "Thinking about {query}" regardless of language.
* **FR-02 (Grounded answers):** MISSING. No retrieval logic exists.
* **FR-03 to FR-04 (Evidence):** MISSING.
* **FR-05 (PDF Viewer):** STUB. Hardcoded HTML div.
* **FR-06 (Scheme registry):** PARTIAL. Models exist in DB, but `registry/schemes.yaml` is missing and no endpoints exist.
* **FR-07 to FR-11 (Discovery, Scraping, Invalidation):** MISSING.
* **FR-12 to FR-15 (Eligibility):** STUB. A disconnected `EligibilityEvaluator` python class exists.
* **FR-16 to FR-26:** MISSING.

### Integrity Rules (§0.3)
All integrity rules are effectively MISSING because the systems they govern (auto-publishing, authoritative sources, rule invalidation, crawl policies) do not exist.
* **Fake success rule:** VIOLATION. If no API key is provided, the UI shows a "successful" fake response instead of failing gracefully.

### Phase Gates (§17)
* **Phase 0:** PASS. Backend starts, frontend starts, empty DB migration passes, no secrets committed.
* **Phase 1-14:** MISSING/STUB.

## 5. Commands Run
* `tree -L 4 -I "node_modules|.git|.venv|__pycache__|dist|build"` -> Showed 35 directories, 40 files.
* `python -c "import app.main; ..."` -> Backend imports OK.
* `uvicorn app.main:app &` -> Started server on 8000.
* `curl -s http://127.0.0.1:8000/health` -> `{"status":"ok"}`
* `alembic upgrade head` -> Ran initial migration.
* `pytest tests/` -> 1 passed (dummy test).
* `npm run build` -> Built frontend successfully.
* `grep -Ri "api_key\|ADMIN_TOKEN" .` -> No hardcoded secrets found.
* `curl -s -X POST http://127.0.0.1:8000/api/v1/chat -H "Content-Type: application/json" -d '{"query": "Hello", "language": "en"}'` -> `data: {"token": "Thinking"}`.

## 6. Discrepancies
`docs/IMPLEMENTATION_STATUS.md` correctly lists Phase 0 as `IN_PROGRESS` and everything else as `NOT_STARTED`. This is honest and matches the codebase.

## 7. Dead Code and Extras
* `backend/app/ingest/extract.py` is never called.
* `backend/app/eligibility/evaluator.py` is never called.
* The SQLAlchemy models in `backend/app/db/models.py` are never queried or populated.

## 8. Blocked Items
None. The items are simply missing from the codebase.

## 9. Prioritized Fix List
* **P1 (Core Feature Missing):** Implement Document Ingestion and RAG retrieval in `backend/app/rag/` to fulfill FR-02.
* **P1 (Core Feature Missing):** Connect the frontend PDF Viewer to actual `pdf.js` and extracted bounding boxes (FR-05).
* **P1 (Core Feature Missing):** Implement the Web Scraper and Discovery pipeline (FR-07).
* **P1 (Core Feature Missing):** Build the Eligibility API and UI Questionnaire (FR-12, FR-13).

## 10. Hackathon Demo Readiness
**NO.** The 6-hour vertical slice cannot be demonstrated.
* End-to-end journey (Hindi/English ask -> retrieval -> answer -> citation -> PDF): NO.
* Eligibility journey: NO.
* Admin fixture discovery flow: NO.
* Rule invalidation demonstration: NO.
* PWA / Offline: NO.