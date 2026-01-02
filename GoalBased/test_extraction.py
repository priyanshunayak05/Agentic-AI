import os
from dotenv import load_dotenv
import google.generativeai as genai
from state_manager import extract_info_with_llm

load_dotenv()

def test_extraction():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Skipping test: No API KEY")
        return

    genai.configure(api_key=api_key)
    
    valid_models = ["gemini-1.5-flash", "gemini-pro", "models/gemini-pro-preview-12-2025"]
    ids = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    print(f"DEBUG: Available models: {ids}")

    model_name = "gemini-pro"
    for m in valid_models:
        if m in ids or f"models/{m}" in ids:
            model_name = m
            break
            
    if "models/gemini-pro-preview-12-2025" in ids:
         model_name = "models/gemini-pro-preview-12-2025"

    print(f"Using model: {model_name}")
    model = genai.GenerativeModel(model_name)
    
    text = "Hi, I'm John Doe. My email is john@example.com and I'm a Python developer with 5 years experience."
    print(f"Testing text: {text}")
    
    try:
        result = extract_info_with_llm(text, model)
        print("Result:", result)
        
        assert result.get("name") == "John Doe"
        assert result.get("email") == "john@example.com"
        print("Test Passed!")
    except Exception as e:
        print(f"Test Failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_extraction()
