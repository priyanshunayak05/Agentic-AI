import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from state_manager import GoalState, extract_info_with_llm
from utils import extract_text_from_pdf

load_dotenv()

st.set_page_config(page_title="Goal Based Job Assistant", layout="wide")

# -- Session State Init --
if "state" not in st.session_state:
    st.session_state.state = GoalState()

if "chat" not in st.session_state:
    st.session_state.chat = []

# -- Model Init --
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("GOOGLE_API_KEY not found. Please set it in your .env file.")
    st.stop()

genai.configure(api_key=api_key)

# Auto-select best model
valid_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]

if not valid_models:
    st.error("No valid Gemini models found for this API key.")
    st.stop()

# Prefer flash or pro
model_name = valid_models[0]
for m in valid_models:
    if "flash" in m.lower():
        model_name = m
        break
    if "pro" in m.lower() and "vision" not in m.lower(): # Prefer text-capable pro
        model_name = m

print(f"Selected Model: {model_name}")
model = genai.GenerativeModel(model_name)

# -- Sidebar: Resume Upload --
with st.sidebar:
    st.header("📄 Upload Resume")
    uploaded_file = st.file_uploader("Upload your PDF Resume", type=["pdf"])
    
    if uploaded_file:
        if st.button("Analyze Resume"):
            with st.spinner("Extracting info..."):
                text = extract_text_from_pdf(uploaded_file)
                if text:
                    extracted_data = extract_info_with_llm(text, model)
                    st.session_state.state.update_from_dict(extracted_data)
                    st.success("Resume processed! I've updated your profile.")
                else:
                    st.error("Could not read PDF.")

    st.divider()
    st.subheader("Current Profile")
    st.text(f"Name: {st.session_state.state.name or 'Pending...'}")
    st.text(f"Email: {st.session_state.state.email or 'Pending...'}")
    skills = getattr(st.session_state.state, "skills", None)
    if skills:
        # If list, format nicely
        if isinstance(skills, list):
            skills = ", ".join(skills)

        # Always stringify before slicing to avoid KeyError
        skills = str(skills)
        st.caption(f"Skills: {skills[:50]}...")

    if st.button("🔄 Reset Profile"):
        st.session_state.state = GoalState()
        st.session_state.chat = []
        st.rerun()

# -- Main UI --
st.title("🎯 Best Job Application Assistant")

tab1, tab2, tab3 = st.tabs(["💬 Assistant", "📝 Cover Letter", "🎤 Interview Prep"])

# -- Tab 1: Chat Assistant --
with tab1:
    st.markdown("### Let's build your profile!")
    
    # Display Chat
    for msg in st.session_state.chat:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # User Input
    user_input = st.chat_input("Tell me about your experience...")

    if user_input:
        st.session_state.chat.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        # Extract info from user message
        new_info = extract_info_with_llm(user_input, model)
        st.session_state.state.update_from_dict(new_info)

        # Determine reply
        if st.session_state.state.is_complete():
            reply = "Great! I have your basic details. Check out the **Cover Letter** or **Interview Prep** tabs!"
        else:
            missing = st.session_state.state.missing_fields()
            prompt_text = f"""
            You are a helpful Career Coach.
            The user profile is missing: {', '.join(missing)}.
            
            Current context: {user_input}
            Current state: {str(st.session_state.state)}
            
            Ask ONE friendly, specific question to get the missing information.
            If the user asked a question, answer it first, then ask for missing info.
            """
            try:
                response = model.generate_content(prompt_text)
                reply = response.text
            except Exception as e:
                reply = f"Sorry, I had trouble thinking. Error: {e}"

        st.session_state.chat.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.write(reply)


# -- Tab 2: Cover Letter --
with tab2:
    st.header("Generate Cover Letter")
    
    job_desc = st.text_area("Paste the Job Description here:")
    
    if st.button("Generate Letter"):
        if not st.session_state.state.name:
            st.warning("Please complete your profile in the Chat tab first (at least Name).")
        elif not job_desc:
            st.warning("Please provide a Job Description.")
        else:
            with st.spinner("Writing cover letter..."):
                prompt = f"""
                Write a professional cover letter for {st.session_state.state.name}.
                
                User Profile:
                {str(st.session_state.state)}
                
                Job Description:
                {job_desc}
                
                Keep it engaging, professional, and highlight matching skills.
                """
                try:
                    res = model.generate_content(prompt)
                    st.markdown(res.text)
                except Exception as e:
                    st.error(f"Generation failed: {e}")

# -- Tab 3: Interview Prep --
with tab3:
    st.header("Interview Preparation")
    
    if st.button("Generate Questions"):
        if not st.session_state.state.skills:
            st.warning("I need to know your skills first!")
        else:
            with st.spinner("Thinking of questions..."):
                prompt = f"""
                Generate 5 difficult technical and behavioral interview questions for a candidate with this profile:
                {str(st.session_state.state)}
                
                Also provide brief tips for answering each.
                """
                try:
                    res = model.generate_content(prompt)
                    st.markdown(res.text)
                except Exception as e:
                    st.error(f"Generation failed: {e}")
