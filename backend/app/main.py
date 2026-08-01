from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.mongodb import client
from app.routes.debate import router as debate_router

app = FastAPI(title="The Contrarian")

# Allow React Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    client.admin.command("ping")
    return {
        "message": "The Contrarian Backend is Running!",
        "database": "Connected"
    }


app.include_router(debate_router)