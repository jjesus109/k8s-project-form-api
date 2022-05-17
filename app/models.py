from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel, func


class FormBase(SQLModel):
    name: str
    last_name: str
    age: Optional[int] = None
    position: str
    
class Form(FormBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_date: Optional[datetime] = Field(default_factory=func.now)