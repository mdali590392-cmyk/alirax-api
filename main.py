from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import secrets
import string

app = FastAPI()

# CORS allow for app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home Route - Check if API is live
@app.get("/")
def home():
    return {
        "status": "success",
        "message": "ALIRAX API is Live! 🚀",
        "owner": "Ali Khan",
        "api": "https://alirax-api.vercel.app"
    }

# Generate API Key Route
@app.get("/generate-key")
def generate_key():
    random_part = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(24))
    api_key = f"alirax_sk_{random_part}"
    return {
        "api_key": api_key,
        "status": "active",
        "message": "Your ALIRAX Key Generated Successfully!"
    }

# For testing in browser - /key se bhi kaam karega
@app.get("/key")
def generate_key_short():
    return generate_key()
