from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def hello():
    return {'message':"Hello world"}

@app.get('/about')
def about():
    return {'message':"I am Mahi Sarwar Anol, a fellow Machine Learning Engineer"}