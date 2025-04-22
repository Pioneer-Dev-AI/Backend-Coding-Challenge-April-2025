from typing import Optional

from sqlmodel import SQLModel, Field


class PhoneBook(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    phone_number: str = Field(index=True) 