from typing import Any

from sqlalchemy import ScalarResult, Sequence, select
from sqlalchemy.ext.asyncio import AsyncSession

from core.types import MODEL, TYPE_MODEL


async def get_model(
        session: AsyncSession,
        model: TYPE_MODEL,
        conditions: list[Any] = None
) -> MODEL | None:
    smtp = select(model)
    if conditions is not None:
        smtp = smtp.where(*conditions)
    return await session.scalar(smtp)


async def get_models_by(session: AsyncSession, model: TYPE_MODEL, conditions) -> Sequence[MODEL | None]:
    result: ScalarResult[MODEL] = await session.scalars(select(model).where(*conditions))
    return result.all()


async def create_model(session: AsyncSession, model: TYPE_MODEL, model_in) -> MODEL:
    instance = model(**model_in.model_dump(exclude_unset=True))
    session.add(instance)
    await session.commit()
    await session.refresh(instance)
    return instance


async def update_partial_model(session: AsyncSession, model: TYPE_MODEL, model_in) -> MODEL:
    instance = await get_model(session, model, conditions=[model.id == model_in.id])
    for field, value in model_in.model_dump(exclude_unset=True).items():
        setattr(instance, field, value)
    await session.commit()
    await session.refresh(instance)
    return instance
