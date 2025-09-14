# FastAPI philosophy , how to setup fastapi, installation and code

from fastapi import FastAPI

app = FastAPI()


# decorator through create raout
@app.get ("/")  # get request = only read data (static)
               # post request = user side any input in server that time use post
               # ("/")= in write rout  means rout heat to API work oprn new page any oprection, etc

def hello(): # hello function call name
    return {"massage": "hello world"}   

# file run =       uvicorn 1_main:app --reload 
# /docs  = auto generate documication help to api testing.     
