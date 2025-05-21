from pydantic import BaseModel

class patient(BaseModel):
    name: str
    age: int


def insert_patient_without_pydantic(name,age):
    print(name)
    print(age)
    print('Inserted')


def insert_patient_with_pydantic(patient:patient):
    print(patient.name)
    print(patient.age)
    print('Inserted')


patient_info={'name':'mahi','age': 30}

patient1=patient(**patient_info)

insert_patient_with_pydantic(patient1)