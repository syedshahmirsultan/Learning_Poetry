from fastapi import FastAPI,Query
from typing import Annotated
app:FastAPI = FastAPI()


@app.get("/items",tags=["items"],summary="Getting Items",response_description="Response Description")
def get_items(item:Annotated[str,Query()]): 
    """  
    Description of function
    
    """
    return item


@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]