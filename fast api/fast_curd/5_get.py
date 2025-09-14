# Path & Query Params in FatAPI 
# Path,Params =  specific resoures located
# ex data retrive (only data read) social media pertical peple show the profile
     # update oprection single resource
     # specif resourse delete


#  path endpoint  = the path function in fastapi is used to provide metadata, validation rules, and documentation hints for path parameters
        #  in your API endpoint
 #example, Tile, Description, example, greter than,gt,le,it,min_lenth, maxt length, regex

# exceptions = 
# HTTPException is a special foult-in -exception in FastAPI used to return custom HTTP error response when something goes wrong in your API.
# instead of returing a normal JSONor creating the server. you can gracefully raise an error with
# - a proper HTTP status code (like 404, 400, 403 etc.)
# a custom error massage
# (optical) extra header

# Query Parameter =
# query parameter are optional key-value pairs appended to the end of a URL, used to pass additonal data to the server in an HTTP request.
  # they are typically empoyed for operations like filtering sorting, searching and pagination without altering the endpoint path itself
# /patients?city=Qelhi&sort_by=age

# the ? makes the start of query parameters.
# each parameter is a key-value pair key=value
# multiple parameters are seprated by &

# in the case
# city = Delhi is a query parsmeters for filtering
# sort_by = age is a query paerameter for sorting 

from fastapi import FastAPI , Path, HTTPException, Query
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
def view_patient(patient_id:str = Path(..., description = "ID of the patient in the DB", example = 'P001')):
                                # Path = use input time show the suggestion tip
    #load all the patient data
    data = load_data() # () = All data show in user

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code = 404, detail = "Patient not found")

# sorted show data api

# path parameter means dynamic work its take perticular  source fatch data
# query parameter means  parameter in use seaching, filtering etc


# run to condiction query
# /sort?sort_by=height&order=desc
# /sort?sort_by=weight&order=desc
# /sort?sort_by=bmi&order=desc

@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort on the basis of height, weight, or bmi"),
    order: str = Query("asc", description="Sort in asc or desc order")):

    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400,
                            details = f"invalid field select from {valid_fields}")

    if order not in ["asc", "desc"]:
       raise HTTPException(status_code = 400,
                           details = "Invalid order asc and desc")
      

    data = load_data()

    sort_order = True if order == "desc" else False

    sorted_data = sorted(data.values(),
                         key = lambda x: x.get(sort_by, 0), reverse= False)
    
    return sorted_data    


    

  