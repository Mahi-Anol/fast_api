### to create on crud

from fastapi import FastAPI
import json
from pydantic import BaseModel,Field,computed_field

from typing import Annotated,Literal

app=FastAPI()


class patient(BaseModel):
    id:Annotated[str,Field(...,description='Id of the patient',examples=['P001'])]
    name:Annotated[str,Field(...,description='Name of the patient')]
    city:Annotated[str,Field(...,description='City where the patient is living')]
    age:Annotated[int,Field(...,gt=0,lt=0,description='Age of the patient')]
    gender:Annotated[Literal['male','female','others'],Field(...,description='Gender of the patient')]
    height:Annotated[float,Field(...,gt=0,description='height of the patient in mtr')]
    weight:Annotated[float,Field(...,gt=0,description='Weight of the patient in kg')]

    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/self.height**2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)

def json_file_loader():
    with open('/home/mahi-anol/fast_api/patients.json','r') as f:
        data=json.load(f)
    return data


@app.get("/get_all_users_data")
def get_all_user_data():

    data=json_file_loader()
    return data