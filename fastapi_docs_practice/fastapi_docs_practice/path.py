from fastapi import FastAPI
from typing import Any
from enum import Enum

app : FastAPI = FastAPI()






@app.get("/item/{item_id}")
def get_item_id(item_id:int)->Any:
    '''
    This function will return Item_id provided by the user
    '''
    return {"Item_id" : item_id}



@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# This will execute when user sent request to users route because FastAPI will match this first
@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]



class ModelText(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    

@app.get("/models/{model_name}")
async def get_model(model_name: ModelText):
    """ This function will give response only if the user will provide model_name which is present in ModelText class"""
    if model_name is ModelText.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

#This will give error if you passed this url /hi/hello/hey
@app.get("/hi/{file_path}")
def get_path(file_path):
    return {"Path":file_path}

@app.get("/hello/{file_path:path}")
def get_path_url(file_path):
    """ This function will return the path even if you passed like this /hello/hi/bye"""
    return {"Path":file_path}