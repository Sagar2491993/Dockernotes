from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional

class Patient(BaseModel):
    # data typde validation 
    # optional data means defount data (user does not intert data)
    # data vlidation (use common use case) ex. email, linkedin  but bussiness validation very differnce not use better 
                             # other case use 99_pyd.py
    name: str
    email: EmailStr
    linkedin: AnyUrl
    age: int
    weight: float
    married: bool = False # defolt value
    allergies: Optional[List[str]] = None # patient_info not write data
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
                  "age":32, "weight":66.66 ,#"married": True,
                #"allergies": ["polen", "dust"],
                "contact_details": { "phone": "1234567898"} }

patient1 = Patient(**patient_info) # **patient_info = distionary use that reasion **

insert_patient_data(patient1)
update_patient_data(patient1)
