import datetime

from sqlalchemy import Enum, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column

from core.enums import StatusType, SentimentType, CategoryType
from core.models import Base


class Complaint(Base):
    text: Mapped[str]
    status: Mapped[StatusType] = mapped_column(
        Enum(StatusType),
        default=StatusType.open,
        server_default=StatusType.open.value
    )
    timestamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP,
        default=datetime.datetime.now,
        server_default=func.now()
    )
    sentiment: Mapped[SentimentType] = mapped_column(Enum(SentimentType))
    category: Mapped[CategoryType] = mapped_column(
        Enum(CategoryType),
        default=CategoryType.other,
        server_default=CategoryType.other.value
    )

    def __str__(self):
        return f"Complaint#{self.id}(status={self.status}, sentiment={self.sentiment}, category={self.category}, text={self.text[:30]})"

    def __repr__(self):
        return str(self)