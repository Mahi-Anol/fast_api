from pydantic import BaseModel
from typing import List,Dict

class patient(BaseModel):
    name: str
    age: int
    weight:float
    maried:bool
    allergies:List[str]
    contact_detail:Dict[str,str]


# def insert_patient_without_pydantic(name,age):
#     print(name)
#     print(age)
#     print('Inserted')

def insert_patient_with_pydantic(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.maried)
    print(patient.allergies)
    print(patient.contact_detail)
    print('Inserted')

patient_info={'name':'mahi','age': 30,'weight':70.6,'maried':True,'allergies':['a','b','c'],'contact_detail':{'phone':'018167035255','email':'fff'}}

patient1=patient(**patient_info)

insert_patient_with_pydantic(patient1)