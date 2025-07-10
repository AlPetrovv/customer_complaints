import datetime

from fastapi import APIRouter, BackgroundTasks
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from complaints.models import Complaint
from config import settings

from core.enums import SentimentType, CategoryType, StatusType
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
async def create_complaint(
        complaint_in: schemas.ComplaintCreate,
        background_tasks: BackgroundTasks,
        session: AsyncSession = Depends(db_helper.get_scoped_session)
):
    sentiment = await services.get_sentiment(complaint_in.text)
    if sentiment is not None:
        complaint_in.sentiment = SentimentType(sentiment)
    complaint = await crud.create_complaint(session, complaint_in)
    background_tasks.add_task(services.set_category, complaint_id=complaint.id, text=complaint_in.text, session=session)
    return complaint


@router.get('/', response_model=list[schemas.ComplaintRead])
async def get_complaints(session: AsyncSession = Depends(db_helper.get_scoped_session)):
    timestamp = datetime.datetime.now() - datetime.timedelta(days=3)
    complaint_status = StatusType.open
    return await crud.get_complaints_by(session, conditions=[Complaint.timestamp > timestamp,
                                                             Complaint.status == complaint_status])


@router.patch('/', response_model=schemas.ComplaintRead)
async def update_partial_complaint(
        complaint_in: schemas.ComplaintUpdatePartial,
        session: AsyncSession = Depends(db_helper.get_scoped_session)
):
    return await crud.update_partial_complaint(session, complaint_in)
