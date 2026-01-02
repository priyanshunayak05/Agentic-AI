from pydantic import BaseModel, Field
from typing import Optional, List
import google.generativeai as genai
import json
import re

# Define the data structure we want to extract
class UserProfile(BaseModel):
    name: Optional[str] = Field(description="The user's full name")
    email: Optional[str] = Field(description="The user's email address")
    phone: Optional[str] = Field(description="The user's phone number")
    skills: Optional[str] = Field(description="A comma-separated list of skills")
    experience: Optional[str] = Field(description="Summary of work experience")
    education: Optional[str] = Field(description="Summary of education")
    linkedin: Optional[str] = Field(description="LinkedIn profile URL")

class GoalState:
    def __init__(self):
        self.name = None
        self.email = None
        self.phone = None
        self.skills = None
        self.experience = None
        self.education = None
        self.linkedin = None

    def update_from_dict(self, data: dict):
        """Update state from a dictionary of fields."""
        for key, value in data.items():
            # Filter out null/None/empty strings
            if value and str(value).lower() not in ["null", "none", "n/a"] and not getattr(self, key, None):
                setattr(self, key, value)

    def is_complete(self):
        # Ensure fields are non-empty strings
        return (self.name and len(self.name) > 1 and 
                self.email and len(self.email) > 3 and
                self.skills and len(self.skills) > 1 and 
                self.experience and len(self.experience) > 1)

    def missing_fields(self):
        missing = []
        if not self.name: missing.append("name")
        if not self.email: missing.append("email")
        if not self.skills: missing.append("skills")
        if not self.experience: missing.append("experience (brief summary)")
        return missing

    def __str__(self):
        return f"""
        Name: {self.name}
        Email: {self.email}
        Phone: {self.phone}
        Skills: {self.skills}
        Experience: {self.experience}
        Education: {self.education}
        LinkedIn: {self.linkedin}
        """

def extract_info_with_llm(text: str, model):
    """
    Uses the Gemini Model (native) to extract UserProfile fields.
    """
    prompt = f"""
    You are an expert data extraction assistant.
    Extract the following user information from the text provided below.
    Return ONLY a valid JSON object. Do not include markdown formatting like ```json.
    
    Fields to extract:
    - name
    - email
    - phone
    - skills
    - experience
    - education
    - linkedin
    
    If a field is not found, exclude it or set to null.
    
    Text: {text}
    """
    
    try:
        response = model.generate_content(prompt)
        
        debug_info = f"Feedback: {response.prompt_feedback}\n"
        if not response.parts:
            debug_info += "BLOCKED: No parts returned."
            print(debug_info)
            with open("debug_log.txt", "w", encoding="utf-8") as f:
                f.write(debug_info)
            return {}
            
        with open("debug_log.txt", "w", encoding="utf-8") as f:
            f.write(f"RAW_RESPONSE:\n{response.text}\n")
            
        # Try to find JSON block
        # Try to find JSON block
        json_match = re.search(r"```(?:json)?(.*?)```", response.text, re.DOTALL)
        if json_match:
            cleaned_text = json_match.group(1).strip()
        else:
            cleaned_text = response.text.strip()
            
        return json.loads(cleaned_text)
    except Exception as e:
        print(f"Extraction error: {e}")
        with open("debug_log.txt", "w", encoding="utf-8") as f:
            f.write(f"EXCEPTION: {e}")
        return {}
