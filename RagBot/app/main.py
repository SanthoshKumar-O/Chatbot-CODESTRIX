from app.rag.retriever import retrieve_context
from app.rag.prompt_builder import build_prompt
from app.rag.generator import generate_response
from app.skill.mentor_agent import mentor_agent

while True:
    query=input("\nHow can I assist you in learning today? (Type 'e' to quit):")
    if query.lower()=='e':
        print("Exiting...")
        break
    response=mentor_agent(query)
    print(response)
    print("-"*50)

