from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import Any
app:FastAPI = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: str
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: str
    full_name: str | None = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user

@app.get("/teleport")
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")