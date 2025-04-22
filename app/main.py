from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from sqlmodel import Session

from app.database import engine, create_db_and_tables
from app.schemas import PhoneNumberRequest, PhoneNumberResponse

app = FastAPI()

def get_session():
    with Session(engine) as session:
        yield session


@asynccontextmanager
async def lifespan():
    create_db_and_tables()

@app.post("/lookup", response_model=PhoneNumberResponse)
def lookup_phone_number(
    request: PhoneNumberRequest,
    session: Session = Depends(get_session)
):
    pass

@app.get("/search")
def search_phone_numbers(
    q: str,
    session: Session = Depends(get_session)
):
   pass