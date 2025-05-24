from fastapi import FastAPI,Path,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Optional,Annotated,Literal
import json
app=FastAPI()

class patient(BaseModel):
    id:Annotated[str,Field(...,description='Id of the patient',examples=['P001'])]
    name:Annotated[str,Field(...,description='Name of the patient')]
    city:Annotated[str,Field(...,description='City where the patient is living')]
    age:Annotated[int,Field(...,gt=0,lt=100,description='Age of the patient')]
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
    def verdict(self)->str:
        if self.bmi<18.5:
            return "Under Weight"
        elif self.bmi<25:
            return "Normal"
        else:
            return 'obese'


class patient_update(BaseModel):
    name:Annotated[Optional[str],Field(default=None)]
    city:Annotated[Optional[str],Field(default=None)]
    age:Annotated[Optional[int],Field(default=None,gt=0)]
    gender:Annotated[Optional[Literal['male','female']],Field(default=None)]
    height:Annotated[Optional[float],Field(default=None,gt=0)]
    weight:Annotated[Optional[float],Field(default=None,gt=0)]

def json_file_loader():
    with open('/home/mahi-anol/fast_api/patients.json','r') as f:
        data=json.load(f)
    return data

def save_data(data):
    with open('/home/mahi-anol/fast_api/patients.json','w')as file:
        json.dump(data,file)

@app.put('/edit/{patient_id}')
def update_patient(patient_id:str,patient_update:patient_update): 
    data=json_file_loader()

    if patient_id not in data:
        raise HTTPException(code=404,detail="Patient ID not found")
    
    existing_patient_info=data[patient_id]
    updated_patient_info=patient_update.model_dump(exclude_unset=True)

    for key,value in updated_patient_info.items():
        existing_patient_info[key]=value

    existing_patient_info['id']=patient_id

    patient_pydantic_obj=patient(**existing_patient_info)

    existing_patient_info=patient_pydantic_obj.model_dump(exclude=['id'])

    data[patient_id]=existing_patient_info

    save_data(data)

    return JSONResponse(status_code=200,content={'message':'Update Successsuful'})


@app.delete('/delete/{patient_id}')
def del_patient(patient_id:str):
    data=json_file_loader()

    if patient_id not in data:
        raise HTTPException(status_code=404,detail="Patient id not found")
    del data[patient_id]
    save_data(data)
    return JSONResponse(status_code=200,content={"content": "successfully removed" })

