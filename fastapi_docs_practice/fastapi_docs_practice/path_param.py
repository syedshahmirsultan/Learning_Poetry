from fastapi import FastAPI,Path
from typing import Annotated

app1 :FastAPI = FastAPI()

@app1.get("/{item}")
def get_item(item:Annotated[str |None,Path(title="The ID of the item to get")]):
    return item

@app1.get("/item/{item_id}")
def get_item_id(item_id:int = Path(gt=0,le=1000)):
    return item_id
