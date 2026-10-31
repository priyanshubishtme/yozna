# API Audit

## Inventory
* **POST /api/v1/chat**
  * **Status:** Implemented (but largely mocked).
  * **Parameters:** `ChatRequest` (query: string, language: string)
  * **Response:** Server-Sent Events (SSE) stream. Returns mocked sequence if `GROQ_API_KEY` is not provided.
  * **Test Result:** Streaming works, correctly integrated with frontend. RAG logic is absent (no real document retrieval).

* **GET /health**
  * **Status:** Implemented.
  * **Response:** `{"status": "ok"}`
  * **Test Result:** Works.

## Missing Endpoints
All other endpoints listed in Blueprint Section 12.1 and 12.2 are missing.
* `/schemes`
* `/schemes/{scheme_id}`
* `/schemes/{scheme_id}/documents`
* `/questionnaire`
* `/eligibility/evaluate`
* `/recommendations`
* `/documents/{document_id}/file`
* `/citations/{chunk_id}`
* `/reminders/unsubscribe`
* `/reminders/subscribe`
* All `/admin/*` endpoints.