from fastapi import FastAPI
from starlette.responses import Response, FileResponse, PlainTextResponse
app = FastAPI()

@app.get("/ping")
def ping():
    return  FileResponse ("pong")