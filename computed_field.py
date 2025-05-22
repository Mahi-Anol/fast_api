from pydantic import BaseModel,field_validator,computed_field
from typing import List,Dict

class patient(BaseModel):
    name: str
    age: int
    email:str
    weight:float #kg
    height:float #mtr
    maried:bool
    allergies:List[str]
    contact_detail:Dict[str,str]

    @computed_field(return_type=float)
    @property
    def bmi(self):
        bmi=round(self.weight/self.height**2,2)
        return bmi

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
    print(patient.bmi)
    print('Inserted')

patient_info={'name':'mahi','email':"mahi@icic.com",'age': '30','height':40,'weight':70.6,'maried':True,'allergies':['a','b','c'],'contact_detail':{'phone':'018167035255','email':'fff'}}

patient1=patient(**patient_info)

insert_patient_with_pydantic(patient1)