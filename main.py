from http.client import HTTPException
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from pyexpat import model
from starlette.responses import Response, FileResponse, PlainTextResponse, JSONResponse

app = FastAPI()


class post(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: object

    class characteristics(BaseModel):
        maxspeed: int
        max_fuel_capacity: int

post_stored: List[post] = []


@app.get("/ping")
def ping():
    return FileResponse("pong")


@app.post("/cars")
def create_post(post_payload: List[post]):
    post_stored.extend(post_payload)
    return JSONResponse(content=post, status_code=201, media_type="application/json")


@app.get("/cars")
def list_posts():
    return JSONResponse(content=post_stored, status_code=200, media_type="application/json")


@app.get("/cars/{identifier}")
def read_car(identifier: str):
    for post in post_stored:
        if post.identifier == identifier:
            return JSONResponse(content=post, status_code=200, media_type="application/json")

        raise HTTPException(status_code=404, detail="Car not found")
