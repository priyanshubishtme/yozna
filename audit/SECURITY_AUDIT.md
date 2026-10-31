# Security Audit

## Findings
* **Secret Management:** `.env` is properly ignored in `.gitignore`. `os.getenv` is used to load secrets like `GROQ_API_KEY`.
* **CORS:** Not explicitly configured in FastAPI main app, which could lead to cross-origin issues in a production setup depending on the exact deployment, though currently proxied safely by Vite in local dev.
* **Authentication/Authorization:** Not implemented. The Admin dashboard and secure routes are absent, so there are no exposed administrative controls, but also no security mechanisms enforcing access control as required by the blueprint.
* **Input Validation:** Pydantic is used for the single `/chat` endpoint (`ChatRequest`), which provides basic type safety.
* **SQL Injection:** SQLAlchemy ORM is used, providing basic protection against SQL injection. No raw queries detected.