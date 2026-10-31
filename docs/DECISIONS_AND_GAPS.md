# Decisions and Gaps Register

## Missing Information / Gaps
- `GROQ_IMPLEMENTATION_MASTER_PROMPT.md` was referenced but the instructions were provided in the main system prompt instead.
- We do not have any myScheme authorization (will remain disabled).
- External credentials (Groq, etc.) are needed in `.env`.

## Architectural Decisions
- Using SQLite for local development.
- Python 3.10+ with FastAPI.
- React with Vite, Tailwind CSS, shadcn/ui.
- The 6-hour vertical slice is prioritized without removing long-term product scope.
