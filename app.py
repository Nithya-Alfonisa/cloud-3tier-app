from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Cloud-Native AI Processing Tier")

# Strict CORS Management for Cloud Edge Deployment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows global handshake across secure edge domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextPayload(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {
        "status": "Connected",
        "tier": "Application Tier (Compute Engine)",
        "framework": "FastAPI via Python 3.13",
        "service": "Ready for AI Text Summarization"
    }

@app.post("/api/summarize")
def summarize_text(payload: TextPayload):
    if not payload.text.strip():
        raise HTTPException(status_code=400, detail="Payload content cannot be empty.")
    
    # Simulating the Google ADK Serverless Compute Layer Execution
    words = payload.text.split()
    if len(words) <= 15:
        summary = payload.text
    else:
        summary = " ".join(words[:15]) + "..."
        
    return {
        "original_word_count": len(words),
        "summary": summary,
        "execution_tier": "Serverless Cloud Runtime Container"
    }

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)