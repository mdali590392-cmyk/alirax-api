import os
import hashlib
from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 1. CORS Setup (Security)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://alirax-website.vercel.app", "*"], # Apni site allow karo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Secret keys from Vercel Environment Variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class PromptRequest(BaseModel):
    prompt: str

# 2. Key Verification Function (Hashing)
def verify_alirax_key(api_key: str):
    if not api_key or not api_key.startswith("alx_"):
        raise HTTPException(status_code=401, detail="Invalid ALIRAX API Key format")
    # Yahan hash check ka logic aayega
    return True

@app.get("/")
def home():
    return {"status": "ALIRAX AI Backend is Active & Secure 🔥"}

@app.post("/v1/chat")
def alirax_orchestrator(request: PromptRequest, x_alirax_key: str = Header(None)):
    # Key check
    verify_alirax_key(x_alirax_key)
    
    # ALIRAX Steering Logic (Background AI Call)
    # Piche se Gemini / ChatGPT ko call karega aur user ko ALIRAX ban ke answer dega
    user_prompt = request.prompt
    
    # Dummy Response Example (Yahan backend routing logic aayegi)
    return {
        "provider": "ALIRAX AI Engine",
        "result": f"ALIRAX Processed: {user_prompt}"
    }
