from fastapi import FastAPI,Cookie, Header
from typing import Annotated

from pydantic import BaseModel
app : FastAPI = FastAPI()

@app.post("/item")
def get_item(item:Annotated[str|None,Cookie()] =None):
    return item

@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"user-agent": user_agent}

class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/itemdata/")
async def read_items3(headers: Annotated[CommonHeaders, Header()]):
    return headers