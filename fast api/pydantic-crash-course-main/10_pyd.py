from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    # data typde validation 
    # optional data means defount data (user does not intert data),   optional= datatype
    # data vlidation (use common use case) ex. email, linkedin  but bussiness validation very differnce not use better 
                             # other case use 99_pyd.py
    # custom data validation by use Field function
    # Field purpase other use add metadata means add discription show in 10_pyd.py
    # field and annotated combination use in metadata ex, title , distription, suggestion input example

    name: Annotated[str, Field(max_legth = 50, title ="name of the patioent", discription = "Give me the  name of the " \
    "patioent in less than 50 chars", example = ["Nitish", "Amit"])] # in the data validation and add metadata
    email: EmailStr
    linkedin: AnyUrl
    age: int = Field(gt=0, lt=32) # custom data under 32 it range
    weight: Annotated[float, Field(gt= 0, strict = True)] # strict = dont type version change
    married: Annotated[bool, Field(default = None, Description = "is the patient married or unmarried")] 
    allergies: Annotated[Optional[List[str]], Field(default = None, max_length = 5)]
    contact_details: Dict[str, str]


def insert_patient_data(patient: Patient):  # patient = varible in class ,  Patient = class name
    print(patient.name)  # varible in dict key call
    print(patient.age)
    print(patient.email)
    print(patient.linkedin)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inserted")

def update_patient_data(patient: Patient):  # patient = varible in class ,  Patient = class name
    print(patient.name)  # class in data call
    print(patient.age)
    print("updated")

  
patient_info = {"name": "nitish","email":"abc@gmail.com",
                "linkedin":"http://linkedin.com1234",
                  "age":30, "weight":66.66 ,#"married": True,
                #"allergies": ["polen", "dust"],
                "contact_details": { "phone": "1234567898"} }

patient1 = Patient(**patient_info) # **patient_info = distionary use that reasion **

insert_patient_data(patient1)
update_patient_data(patient1)
