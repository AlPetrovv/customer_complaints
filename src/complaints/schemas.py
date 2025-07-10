import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from core.enums import CategoryType, SentimentType, StatusType


class Complaint(BaseModel):
    text: str
    status: StatusType = Field(default=StatusType.open)
    category: CategoryType = Field(default=CategoryType.other)
    sentiment: SentimentType
    timestamp: datetime.datetime = Field(frozen=True, default_factory=datetime.datetime.now)

    model_config = ConfigDict(from_attributes=True)

class ComplaintCreate(Complaint):
    sentiment: SentimentType = Field(default=SentimentType.unknown)

class ComplaintUpdatePartial(BaseModel):
    id: int
    status: Optional[StatusType] = None
    category: Optional[CategoryType] = None


class ComplaintRead(Complaint):
    id: int


