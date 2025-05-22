from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

from decimal import Decimal

class patient(BaseModel):
    name: Annotated[str,Field(max_length=50,title='Name of the patient',description="name of the patient in 50 charecters",examples=['Nititsh','Amit'],default='MEIN')]
    age: int
    email:EmailStr
    phone_no:Decimal=Field(max_digits=11)
    url:AnyUrl
    weight:Annotated[float,Field(gt=0,strict=True)]
    maried:bool = False ## Cannot assign None when creating object for this one.
    allergies:Annotated[Optional[List[str]],Field(max_length=4,default=None)] ## Can assign None when needed.
    contact_detail:Dict[str,str]

# def insert_patient_without_pydantic(name,age):
#     print(name)
#     print(age)
#     print('Inserted')

def insert_patient_with_pydantic(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.phone_no)
    print(patient.url)
    print(patient.weight)
    print(patient.maried)
    print(patient.allergies)
    print(patient.contact_detail)
    print('Inserted')

patient_info={'name':'mahi','email':'aba@mail.com','phone_no':16700763,'url':'https://www.mahi.com.uk','age': 30,'weight':2,'allergies':None,'maried':True,'contact_detail':{'phone':'018167035255','email':'fff'}}

patient1=patient(**patient_info)

insert_patient_with_pydantic(patient1)