from fastapi import FastAPI,Query
from typing import Annotated,Union

app : FastAPI = FastAPI()


@app.get("/items")
def get_items(item:Annotated[str | None,Query(max_length=50)] = None):
    return item


@app.get("/item")
def get_item(item:Annotated[Union[str,None],Query(max_length=100)] = None):
    return item

@app.get("/user")
def get_user(item:Union[str,None] = Query(default=None,max_length=100, regex="bcd@gmail.com")):
    return item

@app.get("/abcd")
def func1(data:Annotated[list[str],Query(min_length=2,max_length=50,title="Query String",alias="item-query",description="Enter data")] = ["foo","ji"]):
    return data

@app.get("/xyz")
def func1(data:Annotated[list[str],Query(min_length=2,max_length=50,title="Query String",alias="item-query",deprecated=True)] = None):
    return data
    
