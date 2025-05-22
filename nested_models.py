from pydantic import BaseModel


class Address(BaseModel):
    city:str
    state:str
    pincode:str


class Patient(BaseModel):

    name:str
    gender:str
    surn_name:str='raki'
    age:int
    address:Address


address_dict={'city':'Dhaka','state':'Tali office','pincode':'1205'}

address=Address(**address_dict)

patient_dict={'name':"mahi","gender":'male','age':32,'address':address}

patient=Patient(**patient_dict)

def print_p(patient):
    print(patient.name)
    print(patient.gender)
    print(patient.age)
    print(patient.address)
    print(patient.address.city)

print_p(patient)



### taking as dict

temp=patient.model_dump(include=['name','gender']) ### if include parameter not passed, then everything is stored.

print(temp)
print(type(temp))


#taking as json


temp=patient.model_dump_json(exclude=['address'],exclude_unset=True)

print(temp)
print(type(temp))