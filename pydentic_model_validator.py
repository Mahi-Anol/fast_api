from pydantic import BaseModel,field_validator,model_validator
from typing import List,Dict,Optional

class patient(BaseModel):
    name: str
    age: int
    email:str
    weight:float
    maried:bool
    emergancy:Optional[str]=None
    allergies:List[str]
    contact_detail:Dict[str,str]


    @model_validator(mode='after')

    def validate_emergancy_contact(cls,model):
        if model.age>60 and model.emergancy==None:
            raise ValueError('Patients older than 60 must have an emergancy number.')
        return model



# def insert_patient_without_pydantic(name,age):
#     print(name)
#     print(age)
#     print('Inserted')

def insert_patient_with_pydantic(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.maried)
    print(patient.allergies)
    print(patient.contact_detail)
    print('Inserted')

patient_info={'name':'mahi','email':"mahi@icic.com",'age': '70','emergancy':'012044','weight':70.6,'maried':True,'allergies':['a','b','c'],'contact_detail':{'phone':'018167035255','email':'fff'}}

patient1=patient(**patient_info)

insert_patient_with_pydantic(patient1)