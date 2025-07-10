from enum import Enum


class StatusType(str, Enum):
    open = "open"
    closed = "closed"

class SentimentType(str, Enum):
    positive = "positive"
    negative = "negative"
    neutral = "neutral"
    unknown = "unknown"

class CategoryType(str, Enum):
    payment = "payment"
    technical = "technical"
    other = "other"
