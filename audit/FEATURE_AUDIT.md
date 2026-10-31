# Feature Audit

* **Chat Interface:** PARTIALLY IMPLEMENTED. Basic React UI streaming dummy or simple LLM response. State mutation bug identified during previous testing. No actual RAG retrieval.
* **PDF Viewer:** MOCK. A placeholder React component `PDFViewer.tsx` exists with hardcoded HTML and simulated yellow highlight boxes. It does not integrate `pdf.js` or take actual coordinate overlays.
* **Eligibility Evaluator:** BACKEND ONLY. A basic Python class exists but lacks real endpoint integration, database rules retrieval, or front-end questionnaire.
* **Scraper and Scraper Scheduler:** PARTIALLY IMPLEMENTED. APScheduler is set up in `backend/app/scheduler/run.py` but only runs a print-statement mock job. No actual web scraping logic exists.
* **Document Ingestion:** BACKEND ONLY. `backend/app/ingest/extract.py` provides a basic PyMuPDF wrapper to pull words and bounding boxes, but it is not integrated into a complete pipeline.
* **Vector Store/RAG:** BACKEND ONLY. `backend/app/rag/vector_store.py` initializes a Chroma client, but there is no code to populate it or query it.
* **Admin Dashboard:** NOT IMPLEMENTED.
* **PWA & Voice:** NOT IMPLEMENTED.
* **3D Landing Page:** NOT IMPLEMENTED. `apps/web/src/pages/Landing.tsx` is a basic static page.
* **Government Source Registry:** PARTIALLY IMPLEMENTED. SQLAlchemy models exist in `backend/app/db/models.py`, but there are no CRUD API endpoints.