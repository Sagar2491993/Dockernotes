from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    # data typde validation 
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


def insert_patient_data(patient: Patient):  # patient = varible in class ,  Patient = class name
    print(patient.name)  # varible in dict key call
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inserted")

def update_patient_data(patient: Patient):  # patient = varible in class ,  Patient = class name
    print(patient.name)  # class in data call
    print(patient.age)
    print("updated")


patient_info = {"name": "nitish", "age":32, "weight":66.66 ,"married": True,
                "allergies": ["polen", "dust"],
                "contact_details": {"email":"abc@gmail.com", "phone": "1234567898"} }

patient1 = Patient(**patient_info) # **patient_info = distionary use that reasion **

insert_patient_data(patient1)
update_patient_data(patient1)
