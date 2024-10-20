from fastapi import Body, FastAPI,Query
from pydantic import BaseModel
from typing import Annotated


app :FastAPI = FastAPI()

class Item(BaseModel):
    item_name:str
    color:str

class User(BaseModel):
    username:str
    password:str


@app.post('/item')
def get_info(item:Annotated[Item,Body()], user:User):
    return {"item":item, "user":user}
    
    
# @app.post('/user')
# def get_info1(item:Annotated[Item,Query()], user:Annotated[User,Query()]):
#     return {"item":item, "user":user}
    
    
@app.post("/user")
def update_Item(item:Item,user:User,client:Annotated[str,Body(embed=True)]):
    return {"item":item, "user":user,"client":client}


@app.post("/testing")
def update_Item1(item:Annotated[Item,Body()]):
    return {"client":item}


    