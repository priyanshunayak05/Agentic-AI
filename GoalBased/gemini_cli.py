from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from state_manager import GoalState, extract_field
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

state = GoalState()

print("\nGoal Based CLI Assistant\n")

while not state.is_complete():
    user = input("You: ")

    for field in ["name", "email", "skills"]:
        if getattr(state, field) is None:
            v = extract_field(user, field)
            if v:
                setattr(state, field, v)

    if state.is_complete():
        break

    missing = state.missing_fields()[0]

    prompt = f"We ONLY need {missing}. Ask one short question only."
    print("Assistant:", model.invoke(prompt).content)

print("\n🎯 Goal Completed!")
print("Name:", state.name)
print("Email:", state.email)
print("Skills:", state.skills)
