# 🚀 AI Career Assistant — Job Hunter

**Your intelligent companion for landing your dream job.**  
This AI-powered application helps you build a professional profile, generate tailored cover letters, and practice for interviews—all based on your unique resume and experience.

## 🌐 Deployments

You can view the live application at:
- **Streamlit Cloud:** [https://job-hunt-ai.streamlit.app/](https://job-hunt-ai.streamlit.app/)
- **Render:** [https://job-assistant-czhd.onrender.com/](https://job-assistant-czhd.onrender.com/)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://job-hunt-ai.streamlit.app/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-black?style=flat&logo=render)](https://job-assistant-czhd.onrender.com/)

---

![Demo Preview](assets/demo.png)
*(Add a screenshot of your app here in an `assets` folder named `demo.png`)*

---

## 🌟 Features

### 1. 📄 intelligent Resume Parsing
- Upload your PDF resume, and the AI automatically extracts your name, contact info, skills, and experience.
- Uses **Gemini 1.5** to intelligently parse unstructured text into a structured profile.

### 2. 💬 Interactive Chat Assistant
- A "ChatGPT-like" experience tailored for career coaching.
- The assistant notices missing profile details and asks friendly follow-up questions to complete your profile.
- **Reactive UI:** Smooth chat interface with a fixed bottom input bar.

### 3. 📝 Custom Cover Letter Generator
- Paste a Job Description (JD), and the AI generates a professional, engaging cover letter.
- It highlights *your* specific skills that match the JD requirements.

### 4. 🎤 Interview Preparation
- Generates 5 difficult, tailored technical and behavioral questions based on your specific profile.
- Provides tips and strategy advice for answering each question.

### 5. 🔄 Robust Model Switching
- Automatically detects API rate limits (`429 Errors`).
- Seamlessly switches between **Gemini Pro** and **Gemini Flash** models to ensure uninterrupted service.

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/) (Python-based web UI)
- **AI/LLM:** [Google Gemini API](https://ai.google.dev/) (gemini-1.5-flash, gemini-pro)
- **PDF Processing:** `pypdf` / `pymupdf` (fitz)
- **Data Validation:** `Pydantic` for structured data consistency.
- **Environment Management:** `python-dotenv`

---

## 📂 Project Structure

```text
GoalBased/
├── .env                 # API Keys (Not pushed to GitHub)
├── app.py               # Main application entry point (Streamlit UI & Logic)
├── state_manager.py     # Data models & Gemini extraction logic
├── utils.py             # Helper function to read PDF files
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

### Key Files Explained
- **`app.py`**: The heart of the app. Handles the UI layout, chat event loop, and coordinates features.
- **`state_manager.py`**: Manages the user's session state ("memory") and talks to the LLM to extract data.
- **`utils.py`**: Simple utilities for file handling.

---

## 🚀 How to Run Locally

Follow these steps to set up the project on your machine.

### Prerequisites
- Python 3.10 or higher installed.
- A Google Cloud API Key for Gemini. [Get one here](https://aistudio.google.com/app/apikey).

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/priyanshunayak05/Agentic-AI.git
   cd Agentic-AI/GoalBased
   ```

2. **Create a virtual environment (Optional but recommended):**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a file named `.env` in the `GoalBased` folder.
   - Add your API key:
     ```text
     GOOGLE_API_KEY=your_actual_api_key_here
     ```

5. **Run the application:**
   ```bash
   streamlit run app.py
   ```
   The app will automatically open in your browser at `http://localhost:8501`.

---

## 💡 Usecases

- **Job Seekers:** Quickly tailor resumes and cover letters for multiple job applications.
- **Students:** Practice for interviews with questions specifically designed for their skillset.
- **Recruiters:** (Potential extension) Could be adapted to parse incoming resumes and screen candidates.

---

Made with ❤️ by [Priyanshu Nayak](https://github.com/priyanshunayak05)
