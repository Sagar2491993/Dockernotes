def inser_patient_data(name: str, age: int, email:):  #suggest data type but every type accepts
    
    # type validation and data val;idation
    if type(name) == str and type(age) == int:
        if age <0:
            raise ValueError("Age can not negative")
        else:
            print(name)
            print(age)
            print("inserted into database")
    else:
        raise TypeError("incoorect data type")

inser_patient_data("sagar", 32)

def update_patient_data(name: str, age: int):  #suggest data type but every type accepts
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("updated")
    else:
        raise TypeError("incoorect data type")
        
update_patient_data("sagar", 32)

# but in wqeekpoint
# data validation



