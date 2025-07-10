from complaints.models import Complaint
from core.models import Base
models = (Base, Complaint)

__all__ = [model.__class__.__name__ for model in models].append("models")