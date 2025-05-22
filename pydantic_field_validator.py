from pydantic import BaseModel,field_validator
from typing import List,Dict

class patient(BaseModel):
    name: str
    age: int
    email:str
    weight:float
    maried:bool
    allergies:List[str]
    contact_detail:Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domain=['hdfc.com','icic.com']
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domain:
            raise ValueError('Not a valid domain')
        else:
            return value
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age',mode='after') ###when mode set to before it wont woork because in that case it works before type casting.
    @classmethod
    def age_validator(cls,value):
        if 0 <value<50:
            return value
        else:
            raise ValueError('value of age should be between 0 to 50')


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

patient_info={'name':'mahi','email':"mahi@icic.com",'age': '30','weight':70.6,'maried':True,'allergies':['a','b','c'],'contact_detail':{'phone':'018167035255','email':'fff'}}

patient1=patient(**patient_info)

insert_patient_with_pydantic(patient1)