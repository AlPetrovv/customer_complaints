from typing import Any

from sqlalchemy import Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from core import crud
from core.crud import create_model

from .models import Complaint
from .schemas import ComplaintCreate, ComplaintUpdatePartial


async def create_complaint(session: AsyncSession, model_in: ComplaintCreate) -> Complaint:
    return await create_model(session, Complaint, model_in)


async def update_partial_complaint(session: AsyncSession, model_in: ComplaintUpdatePartial) -> Complaint:
    return await crud.update_partial_model(session, Complaint, model_in)


async def get_complaints_by(session: AsyncSession, conditions: list[Any]) -> Sequence[Complaint | None]:
    return await crud.get_models_by(session, Complaint, conditions)
