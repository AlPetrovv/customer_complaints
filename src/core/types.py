from typing import Type, Union

from db.all_models import Base, Complaint

MODEL = Union[Base, Complaint ]
TYPE_MODEL = Type[MODEL]

