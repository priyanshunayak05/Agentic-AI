# Project Knowledge Transfer: Job Application Assistant

This document provides a detailed overview of the files in the `GoalBased` project directory. It is intended to help new developers or collaborators understand the structure and purpose of each component.

## Core Application Files

### 1. `app.py`
**Purpose:** The main entry point and "brain" of the application.
**Key Responsibilities:**
- **UI Rendering:** Uses Streamlit to build the web interface (Chat, Cover Letter, Interview Prep tabs).
- **Session Management:** Initializes and manages `st.session_state` for chat history, user profile data (`GoalState`), and model selection.
- **Model Logic:** Configures the Gemini API, handles model selection (Flash vs Pro), and implements the `run_with_retry` logic to handle API rate limits (429 errors).
- **Event Loop:** Manages the chat flow, capturing user input, generating AI responses, and updating the UI reactively.

### 2. `state_manager.py`
**Purpose:** The data layer and logic for extracting structured information.
**Key Responsibilities:**
- **Data Models:** Defines the `UserProfile` Pydantic model and the `GoalState` class to store user details (Name, Skills, Experience, etc.).
- **Extraction Logic:** Contains the `extract_info_with_llm` function, which uses the LLM to parse unstructured text (chat messages or resumes) into the structured `UserProfile` format.
- **Error Propagation:** Explicitly handles and re-raises `429` errors so the main app knows when to switch models.

### 3. `utils.py`
**Purpose:** Helper functions for file processing.
**Key Responsibilities:**
- **PDF Parsing:** Contains `extract_text_from_pdf(file)`, which utilizes `pypdf` to read text content from uploaded resume files.

### 4. `.env`
**Purpose:** Configuration for sensitive secrets.
**Key Responsibilities:**
- Stores environment variables.
- **Critical Variable:** `GOOGLE_API_KEY` is required here for the Gemini API to function.
- *Note: This file is ignored by git for security.*

## Deployment & Configuration

### 5. `requirements.txt`
**Purpose:** Dependency management.
**Key Responsibilities:**
- Lists all Python packages required to run the project.
- **Key Packages:** `streamlit`, `google-generativeai`, `python-dotenv`, `pypdf`, `pydantic`.

### 6. `render.yaml`
**Purpose:** Infrastructure as Code (IaC) for Render deployment.
**Key Responsibilities:**
- Defines the service type (Web Service).
- Specifies the build command (`pip install -r requirements.txt`).
- Specifies the start command (`streamlit run app.py`).
- Sets the Python version (3.11.9).

### 7. `Procfile`
**Purpose:** Process file for PaaS platforms (like Heroku or Render).
**Key Responsibilities:**
- explicit instruction on how to start the app server: `web: streamlit run app.py`.

## Testing & Auxiliary Files

### 8. `test_extraction.py`
**Purpose:** Unit/Integration testing script.
**Key Responsibilities:**
- A standalone script to verify that `state_manager.py` correctly extracts information from a sample text or resume without running the full web UI.

### 9. `debug_log.txt`
**Purpose:** Runtime logging.
**Key Responsibilities:**
- Automatically created by `state_manager.py` to log raw API responses or errors during the extraction process. Useful for debugging specific failures.

### 10. `debug_gemini.py`, `gemini_cli.py`, `ollama_cli.py`
**Purpose:** Scratchpad scripts.
**Key Responsibilities:**
- These appear to be leftovers from initial API testing or experiments with other models (Ollama). They are not used in the production `app.py` flow.
