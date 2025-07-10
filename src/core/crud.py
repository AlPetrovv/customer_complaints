from typing import Any

from sqlalchemy import ScalarResult, Sequence, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from core.types import MODEL, TYPE_MODEL


async def get_model(
        session: AsyncSession,
        model: TYPE_MODEL,
        conditions: list[Any] = None
) -> MODEL|None:
    smtp = select(model)
    if conditions is not None:
        smtp = smtp.where(*conditions)
    return await session.scalar(smtp)


async def get_all(session: AsyncSession, model: TYPE_MODEL) -> Sequence[MODEL]:
    result: ScalarResult[MODEL] = await session.scalars(select(model))
    return result.all()


async def get_all_by(session: AsyncSession, model: TYPE_MODEL, conditions) -> Sequence[MODEL]:
    result: ScalarResult[MODEL] = await session.scalars(select(model).where(*conditions))
    return result.all()


async def create_model(session: AsyncSession, model: TYPE_MODEL, model_in) -> MODEL:
    instance = model(**model_in.model_dump(exclude_unset=True))
    session.add(instance)
    await session.commit()
    await session.refresh(instance)
    return instance


async def update_partial_model(session: AsyncSession, model: TYPE_MODEL, model_in) -> MODEL:
    instance = await get_model(session, model, model_in.id)
    for field, value in model_in.model_dump(exclude_unset=True).items():
        setattr(instance, field, value)
    await session.commit()
    await session.refresh(instance)
    return instance


async def update_model(session: AsyncSession, model: TYPE_MODEL , model_in) -> MODEL:
    instance = model(**model_in.model_dump())
    await session.commit()
    await session.refresh(instance)
    return instance


async def delete_model(session: AsyncSession, instance) -> None:
    await session.delete(instance)
    await session.commit()


async def get_model_with(session: AsyncSession, model: TYPE_MODEL, options: dict[str, list[Any]], conditions: Any = None) -> MODEL|None:
    smtp = select(model).options(
        *[selectinload(rel_model) for rel_model in options.get('selectinload', [])],
        *[joinedload(rel_model) for rel_model in options.get('joinedload', [])]
    )
    if conditions is not None:
        smtp = smtp.where(*conditions)
    return await session.scalar(smtp)


async def get_all_model_with(session: AsyncSession, model: TYPE_MODEL, options: dict[str, list[Any]], conditions: Any = None) -> Sequence[MODEL]:
    smtp = select(model).options(
        *[selectinload(rel_model) for rel_model in options.get('selectinload', [])],
        *[joinedload(rel_model) for rel_model in options.get('joinedload', [])]
    )
    if conditions is not None:
        smtp = smtp.where(*conditions)
    scalar_result: ScalarResult[MODEL] = await session.scalars(smtp)
    return scalar_result.all()


