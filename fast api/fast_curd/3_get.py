# Next Path and Query Params in # sample demo
# get method in use fast api
# HTTP methos in fastapi
from fastapi import FastAPI 
import json 


app = FastAPI()  # ✅ Create an instance of FastAPI


# creat end point , show the store data in json format
def load_data(): # its json data load
    with open ("patients.json","r") as f:
       data =  json.load(f)
    return data



@app.get("/")# hent in url , path defind
def hello():
    return {"message": "Hello World"}


@app.get("/about")# hent in url , path defind
def about():
    return {"message": "SAGAR ABHANG"}

# new point creat looking json data through raout
@app.get("/view")
def view():
    data = load_data() # () must important other vise dont show data
    return data


   

