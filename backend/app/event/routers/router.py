from fastapi import APIRouter

event_router = APIRouter()


@event_router.get("/")
async def test_get_event():
    return {"status": "OK"}