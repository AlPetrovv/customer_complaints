from complaints.handlers import router as api_complaints_router
from fastapi import APIRouter

api_router = APIRouter(prefix="/api", tags=["api"])
api_router.include_router(api_complaints_router)