from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.event.routers.router import event_router

app = FastAPI(title="Playmate Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(event_router, prefix="/event", tags=["Event"])