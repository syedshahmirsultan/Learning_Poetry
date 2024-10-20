from fastapi import FastAPI


app : FastAPI = FastAPI(title="Query Parameter Practice")


@app.get("/")
def get_user(username:str, email:str):
    return {
        "username":username,
        "email" :email
        }
    
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

@app.get("/user/{user_id}")
async def read_user_item2(
    user_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": user_id, "needy": needy, "skip": skip, "limit": limit}
    return item