from app.rag.retriever import retrieve_context
from app.rag.prompt_builder import prompt
from app.rag.generator import generate_response

while True:
    query=input("\nHow can I assist you in learning today? (Type 'e' to quit):")
    if query.lower()=='e':
        print("Exiting...")
        break
    context=retrieve_context(query)
    prompt=prompt(query,context)
    response=generate_response(prompt)

    print(response)
    print("-"*50)