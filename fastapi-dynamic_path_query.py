from fastapi import FastAPI,Path,HTTPException,Query
import json
app=FastAPI()

def json_file_loader():
    with open('/home/mahi-anol/Neural_Network_from_Scratch/fast_api/patients.json','r') as f:
        data=json.load(f)
    return data

@app.get('/patient_data/{patient_id}')
def view_patient(patient_id:str=Path(...,description="Id of the patient in the DB",example="P001")):
    data=json_file_loader()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="Patient not found")
    

@app.get('/sort')
def view_sorted(sort_by:str=Query(...,description="Sort on the basis of height, weight, bmi"),order:str=Query('asc',description="The order to be followed for sorting")):
    
    valid_fields=['height','weight','bmi']
    order_valid=['asc','dsc']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail="Invalid value. Enter height weight or Bmi")
    
    if order not in order_valid:
        raise HTTPException(status_code=400,detail="Invalid value. Enter 'asc' or 'dsc'")
    
    data=json_file_loader()
    
    sort_order=True if order == 'dsc' else False
    sort_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)

    return sort_data