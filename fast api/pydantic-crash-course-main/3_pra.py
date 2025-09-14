def inser_patient_data(name: str, age: int):  #suggest data type but every type accepts
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("inserted into database")
    else:
        raise TypeError("incoorect data type")
        
    

inser_patient_data("sagar", 32)

