from langchain_community.llms import Ollama
from state_manager import GoalState, extract_field

model = Ollama(model="phi3")
state = GoalState()

print("\nOffline Goal Assistant (Ollama)\n")

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
    prompt = f"Ask ONLY for {missing} in one short friendly question."
    print("Assistant:", model.invoke(prompt))

print("\n🎯 Done")
print(state.__dict__)
