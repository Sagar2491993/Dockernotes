from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude_unset=True) #  its dctionary format output
                        # include=["name"] # only out name shoe # specific out show
                        # exclude =["name","gender"] # not show in output 

                        # not show state  (exclude ={"address" : ["sate"]})

                        # user not input write does not ashow in output   exclude_unset=True

# temp = patient1.model_dump_json ()  #  its json formet output its dctionary format output

print(temp)
print(type(temp))
