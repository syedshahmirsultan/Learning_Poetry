from typing import Annotated

from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}


@app.post("/files/")
def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
def create_upload_file(file: UploadFile):
    return {"filename": file.filename}