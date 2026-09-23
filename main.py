from fastapi import FastAPI
import secrets
from pydantic import BaseModel

app = FastAPI(title="ALIRAX AI API")

# Database ki jagah abhi ke liye yahi pe keys save hongi
all_keys = {}

class PromptRequest(BaseModel):
    api_key: str
    prompt: str

# 1. KEY BANANE WALA GATE
@app.get("/")
def home():
    return {"message": "ALIRAX AI API is Live - Made in Bihar"}

@app.get("/generate-key")
def generate_key():
    new_key = f"alirax_sk_{secrets.token_urlsafe(12)}_BiharX"
    all_keys[new_key] = {"usage": 0, "plan": "Free"}
    return {
        "your_api_key": new_key,
        "status": "Active",
        "note": "Isko copy karke safe rakh lo, ye tumhari ALIRAX KEY hai"
    }

# 2. AI KO CHALANE WALA GATE (Stealth Mode)
@app.post("/v1/generate")
def generate_text(data: PromptRequest):
    if data.api_key not in all_keys:
        return {"error": "Galat ALIRAX KEY hai bhai"}
    
    all_keys[data.api_key]["usage"] += 1
    
    # Yaha pe piche se Gemini/ChatGPT ka code lagega
    # Abhi ke liye dummy reply
    return {
        "prompt": data.prompt,
        "answer": f"ALIRAX ne tumhare liye ye banaya: '{data.prompt}' ka result. Piche se kaam ho raha hai par user ko pata nahi chalega.",
        "powered_by": "ALIRAX AI - Hidden Router"
  }
