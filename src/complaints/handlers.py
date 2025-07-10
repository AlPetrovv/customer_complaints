from fastapi import APIRouter, BackgroundTasks
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from config import settings

from core.enums import SentimentType
from db.helper import db_helper

from complaints import schemas
from complaints import services
from complaints import crud

router = APIRouter(
    prefix=settings.api.complaint,
    tags=["complaints"],
)


@router.post("/", response_model=schemas.ComplaintRead, response_model_exclude_none=True,
             status_code=status.HTTP_201_CREATED)
async def create_complaint(complaint_in: schemas.ComplaintCreate,
                           session: AsyncSession = Depends(db_helper.get_scoped_session)):
    sentiment = await services.get_sentiment(complaint_in.text)
    if sentiment is not None:
        complaint_in.sentiment = SentimentType(sentiment)
    complaint = await crud.create_complaint(session, complaint_in)
    await services.get_category(complaint_id=complaint.id, text=complaint_in.text, session=session)
    return complaint
