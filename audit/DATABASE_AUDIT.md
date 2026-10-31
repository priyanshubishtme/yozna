# Database Audit

## Models Evaluated
* **Source:** Implemented
* **Scheme:** Implemented
* **Document:** Implemented
* **DocumentVersion:** Implemented

## Missing Models
* `source_observations`
* `discovery_runs`
* `fetch_attempts`
* `resource_candidates`
* `document_reviews`
* `scheme_documents`
* `pages`
* `chunks`
* `chunk_boxes`
* `chunks_fts`
* `eligibility_rules`
* `rule_document_dependencies`
* `rule_reviews`
* `ingestion_jobs`
* `chat_sessions`, `chat_messages`, `message_citations`
* `saved_scheme_reminders`, `notification_deliveries`, `audit_events`

## Migrations
* Alembic is configured.
* Initial migration `47770d9d23c1_initial_tables.py` covers the 4 existing models.
* Uses local SQLite database (`yojana.db`). No transactions or API endpoints interact with the database yet.