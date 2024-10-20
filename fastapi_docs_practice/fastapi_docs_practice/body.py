from fastapi import FastAPI
from pydantic import BaseModel

app : FastAPI = FastAPI()

class Item(BaseModel):
    name:str
    description:str

@app.post("/items")
def create_item(item:Item)->Item:
    return item


    