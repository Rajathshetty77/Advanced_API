

from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserUpdate(BaseModel):
    id:int

class UserResponse(BaseModel):
    pass