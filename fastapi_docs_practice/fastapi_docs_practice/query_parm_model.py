from fastapi import FastAPI,Query
from typing import Annotated,Literal
from pydantic import BaseModel,Field

app : FastAPI = FastAPI()

class Item(BaseModel):
    model_config={"extra":"ignore"}
    
    id:int = Field(7,gt=0,le=100)
    name:str = Field("abc",max_length=100,min_length=2)
    order_by: Literal["created_at","updated_at"] = "created_at"
    

@app.get("/items")
def get_item(read_item:Annotated[Item,Query()]):
    return read_item