# example

# 1.   client (post request) json format request body information -- server

# 2.   client data validation information ---> pydantic model validet client information

# 3.   json file --> new record add

from fastapi import FastAPI, Path,HTTPException, Query
import json
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal # as use discription add
                              # litreal as use offiction in one choise


app = FastAPI()

############################## 
# pydantic model help -v1
class Patient(BaseModel):
       #id : Annotated[ str, Field(..., description = "id of patient", example = ["P001"])]
       id: Annotated[str, Field(..., description="id of patient", example="P001")]
       name : Annotated[ str, Field(..., description = "name of the patient")]
       city : Annotated[str, Field(..., description = "city where the patient is living ")]
       age : Annotated[ int, Field(..., gt=0, it=120, description = "Age of the patient")]
       gender :Annotated[Literal["male", "female", "other"], str, Field(..., description = "gender of the patient")]
       height :Annotated[ float, Field(..., gt= 0, description= " height of patient in meters")]
       weight :Annotated[ float, Field(..., gt=0, description= "weight of the patient in kg")]

       # any other content need to check fastapi documentation
       @computed_field
       @property
       def bmi(self) -> float:  # -> float = output str
              bmi = self.weight/(self.weight**2)
              return bmi
       
       @computed_field
       @property
       def verdict(self) -> str:
               
              if self.bmi < 18.5:
                return "underweight"
              elif self.bmi < 25:
                    return "normal"
              elif self.bmi < 30:
                    return "normal"
              else:
                    return "obese"
              
##############################################

# database load / othervise database connect help -v3 
def load_data():
    with open("patients.json", "r") as f:
              data = json.load(f)
    return  data

#  crete data after the save data in write clent data help -v4
def save_data(data):
      with open("patients.json", "w") as f:
            json.dump(data, f) 

##############################################
@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get('/about')
def about():
    return {'message': 'A fully functional API to manage your patient records'}

@app.get('/view')
def view():
    data = load_data()

    return data



# create function start -v1
@app.post("/create")
def create_patient(patient:Patient):  # client data  move to pydantic model will be validation data after further process
      
      # load existing data -v2
      data = load_data()


      # check if the patient already exists (unic data through , example- primary data)
        # check the client data id alredy avilable yes or no -v3
      if patient.id in data:
            return HTTPException(status_code=400, detail = "patient already exists")

      # if not exit in patient data will be new patient data add to in the database like id column through start. -v4
      data[patient.id] = patient.model_dump(exclude = ["id"])
            # data[patient.id] = add data (unique id  not mix data , means primary key) 
            # patient.model_dump(exclude = ["id"]) = data convert in dictonary add to start id

      # new data save into the json file -^5
      save_data(data)
      # succesful save datra  200
      return JSONResponse(status_code= 200, content = {"massage":"patient created success"})


# file run
# uvicorn 1_post:app --reload
