from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.mongodb import client
from app.routes.debate import router as debate_router

app = FastAPI(title="The Contrarian")

# CORS Configuration
# Temporary: Allow all origins for deployment.
# After deploying the frontend on Vercel, replace "*" with your Vercel URL.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    client.admin.command("ping")
    return {
        "message": "The Contrarian Backend is Running!",
        "database": "Connected",
        "status": "Healthy"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


app.include_router(debate_router)