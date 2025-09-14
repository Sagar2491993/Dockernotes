# udate data = use put

# example

# 1.   client (post request) json format request body information -- server

# 2.   client data validation information ---> pydantic model validet client information

# 3.   json file --> new record add

from fastapi import FastAPI, Path,HTTPException, Query
import json
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional # Annotated as use discription add
                              # litreal as use offiction in one choise
                             # Optional = optional input , client not any input write will be defaoult accept the input data 


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
              bmi = round(self.weight/(self.weight**2),2)
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
# update method (put method)

class PatientUpdate(BaseModel):

            # id parameter not use , its paimary through update in data
            name :Annotated[Optional[str], Field(default = None)]
            city :Annotated[Optional[str], Field(default = None)]
            age :Annotated[Optional[int], Field(default = None, gt = 0)]
            gender :Annotated[Optional[Literal["male", "female"]], Field(default = None)]
            height :Annotated[Optional[float], Field(default = None, gt = 0)]
            weight :Annotated[Optional[float], Field(default = None, gt = 0)]

              
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
# get method
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

#######################################################
# post method

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

#########################################
# update method (put data)
@app.put("/edit/{patient_id}") # patient_id throgh edit enteral data
def update_patient(patient_id: str, patient_update:PatientUpdate):
                       # patient_id: str = pathparent  through in specific data edit observation and start , its given type is string
                       #  patient_update:PatientUpdate = given to request body data from clent throgh update data, its change data receve and update in new pydantic  object so before create PatientUpdate
                    
                    # load the database data , its use json data , load the json data
                    data = load_data()

                    # if client edit data any specific id , will be check the id prent in database yes or no , will be further process

                    # patient id not present in data
                    if patient_id not in data:
                          raise HTTPException (status_code=404, detail = "patient not found") # patient wrong
                    
                    # patient id  present in data
                    existing_patient_info = data[patient_id] # client input patient id availble, so inter specific id in all fom extract
                                                             # so current exesting dictonary updale from client with change dictionary key
                      # before update to pydantic convert dictionary                                      
                    update_patient_info = patient_update.model_dump(exclude_unset = True) # pydantic convert dictionary
                                                                                          # exclude_unset = True = (all fileld availble from pydantic but use reasion only update paramter from client) 
                    # specific key in valu update not all data edit
                    # for key(city), value(mumbai) in update_patient_info.items():
                    for key, value in update_patient_info.items(): # update data in sort key vise
                          existing_patient_info[key] = value  # same key udate new value data

                          #  existing_patient_info -> pydantic object -> update bmi +verdict -> pydantic object -> dict
                    existing_patient_info["id"] = patient_id
                    patient_pydantic_obj = Patient(**existing_patient_info) # bmi in other calculate dat and convert to pydantic and validate 
                    # again pydantic convert dictionary
                    existing_patient_info = patient_pydantic_obj.model_dump(exclude = "id")
                                                                            # exclude = "id" = ignore id data other all data conver dictionary


                    #  add this dictionary to data
                    data[patient_id] = existing_patient_info
                    # data[patient_id] =  before in data id sequce vice update dada all data store from existing_patient_info

                    # UPDATE SAVE DATA
                    save_data(data)
                    return JSONResponse(status_code=200, content= {"massage":"patient update data"})

####################################################

# delete method
@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    # load data
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient deleted'})





# file run
# uvicorn 1_update_delete:app --reload
