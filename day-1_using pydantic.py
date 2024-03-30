from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app=FastAPI()


class post(BaseModel):
    title: str
    massage: str

@app.get("/")
async def read_root():
    return {"Massage": "Weljcoeeee api"}

@app.post("/mass")
async def post_m(new_post: post):
    print(new_post)
    return {"Your post was":f"{new_post.title}, {new_post.massage}"}
