# Integration Audit

## Groq API (via OpenAI client)
* **Status:** Configured but largely bypassed in local dev if no key is supplied.
* **Credentials:** Read from `GROQ_API_KEY` environment variable.
* **Client:** `AsyncOpenAI`.
* **Conclusion:** API client is implemented but not connected to retrieved documents (RAG context).

## PyMuPDF
* **Status:** Imported in `backend/app/ingest/extract.py`.
* **Usage:** Extracts text and bounding boxes for PDF pages.
* **Conclusion:** Functional locally but entirely disconnected from the main API flow and no uploading mechanism exists.

## ChromaDB
* **Status:** Set up in `backend/app/rag/vector_store.py`.
* **Usage:** Initializes a persistent client at `./data/indexes`.
* **Conclusion:** Database initializes but no data is written or queried. Multilingual embeddings (e.g. `multilingual-e5-base`) are not integrated.