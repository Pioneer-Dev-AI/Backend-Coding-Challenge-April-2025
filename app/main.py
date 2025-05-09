from contextlib import asynccontextmanager

from Levenshtein import distance
from fastapi import FastAPI, Depends, Query
from sqlmodel import Session, select

from app.database import engine, create_db_and_tables
from app.models import PhoneBook
from app.schemas import PhoneNumberRequest, PhoneNumberResponse, PhoneNumberMatch

app = FastAPI()


def get_session():
    with Session(engine) as session:
        yield session


@asynccontextmanager
async def lifespan():
    create_db_and_tables()


@app.get("/lookup", response_model=PhoneNumberResponse)
def lookup_phone_number(
    phone_number: str = Query(..., description="Phone number to look up"),
    session: Session = Depends(get_session)
):
    pass


@app.get("/search", response_model=)
def search_phone_numbers(
    q: str = Query(..., description="Search query (partial phone number)"),
    session: Session = Depends(get_session)
):
  pass
