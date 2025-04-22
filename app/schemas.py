from pydantic import BaseModel

class PhoneNumberRequest(BaseModel):
    phone_number: str

class PhoneNumberMatch(BaseModel):
    name: str
    phone_number: str
    distance: int

class PhoneNumberResponse(BaseModel):
    match: PhoneNumberMatch 