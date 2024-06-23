from pydantic import BaseModel, ConfigDict, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    password: str


class SAccessToken(BaseModel):
    access_token: str

    model_config = ConfigDict(from_attributes=True)


class SUser(BaseModel):
    id: int
    email: EmailStr
    hashed_password: str
