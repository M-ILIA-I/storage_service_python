from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.user_dasboard.api import api_storage_service


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_storage_service)
