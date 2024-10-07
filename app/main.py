from fastapi import FastAPI
from app.user_dasboard.api import api_storage_service


app = FastAPI()

app.include_router(api_storage_service)
