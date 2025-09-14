# Path & Query Params in FatAPI 
# Path,Params =  specific resoures located
# ex data retrive (only data read) social media pertical peple show the profile
     # update oprection single resource
     # specif resourse delete


#  path  = the path function in fastapi is used to provide metadata, validation rules, and documentation hints for path parameters
        #  in your API endpoint
 #example, Tile, Description, example, ge,gt,le,it,min_lenth, maxt length, regex

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


@app.get("/patient/{patient_id}")
def view_patient(patient_id:str):
    #load all the patient data
    data = load_data() # () = All data show in user

    if patient_id in data:
        return data[patient_id]
    return {"massage":"patient not found"}


# Path,Params = advance level use in 5_main.py