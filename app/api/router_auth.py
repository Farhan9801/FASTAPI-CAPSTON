from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.security import create_token


class AuthInput(BaseModel):
    username: str
    password: str

route = APIRouter()


@route('/login')
def login(auth: AuthInput):
    if auth.username == "admin" and auth.password=="admin":
        token = create_token({"sub" : auth.username})
        return {"access_token" : token}
    return HTTPException(403, detail="Invalid Credential")