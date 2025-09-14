# sample demo
# get method in use fast api
from fastapi import FastAPI 

app = FastAPI()  # ✅ Create an instance of FastAPI

@app.get("/")# hent in url , path defind
def hello():
    return {"message": "Hello World"}


@app.get("/about")# hent in url , path defind
def about():
    return {"message": "SAGAR ABHANG"}




