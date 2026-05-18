from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .app.database import engine, Base
from .app.routers import auth, sessions, chat

# Create database tables directly on startup for robustness
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Personalized Learning Recommender Chatbot API",
    description="FastAPI Backend powered by Groq & local ChromaDB RAG",
    version="1.0.0"
)

# CORS configurations
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict to Vercel/frontend domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth.router)
app.include_router(sessions.router)
app.include_router(chat.router)

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "service": "learning-recommender-api"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
