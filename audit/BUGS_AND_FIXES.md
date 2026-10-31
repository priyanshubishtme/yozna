# Bugs and Fixes

## Resolved Defects
* **React State Mutation (Fixed during Pre-commit check):** The chat streaming interface incorrectly updated state using a mutated object `newMsgs[newMsgs.length - 1].content += data.token`, which caused duplicated text in React Strict mode. This was fixed by correctly copying the object.

## Outstanding Defects & Business Logic Gaps
* **Missing RAG Integration:** The `ChatInterface` connects to a mocked backend endpoint if no API key is provided, or a generic LLM pass-through if it is. It does not perform vector searches on ChromaDB or parse actual government documents.
* **Missing Eligibility Workflows:** The `EligibilityEvaluator` Python class exists but is not invoked by any endpoint. The frontend questionnaire does not exist.
* **Missing Admin Pipeline:** There is no way to trigger the APScheduler jobs via an API, nor a UI to review scraped documents.
* **Fake PDF Viewer:** The `PDFViewer` component is a hardcoded mock. It does not load a real PDF or apply the bounding boxes from PyMuPDF.