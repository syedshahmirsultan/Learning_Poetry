from fastapi import FastAPI


app : FastAPI = FastAPI()

@app.get("/")
def index()->str:
    return "Hello World !"

@app.get("/piaic")
def piaic()->dict:
    return {"organization" : "PIAIC"}