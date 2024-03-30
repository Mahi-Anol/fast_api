from fastapi import FastAPI
from fastapi.params import Body

app=FastAPI()

@app.get("/")
async def read_root():
    return {"Massage": "Welcoeeee api"}

@app.post("/mass")
async def post_m(payload: dict=Body(...)):
    print(payload)
    return {"Your post was":f"{payload['title']}, {payload['massage']}"}
