from fastapi import FastAPI
import json


app=FastAPI()


def json_file_loader():
    with open('D:\Fast-api\patients.json','r') as f:
        data=json.load(f)
    return data


@app.get("/get_all_users_data")
def get_all_user_data():

    data=json_file_loader()
    return data

@app.get("/get_specific_user_data")
def get_specific_user_data(user_id):

    data=json_file_loader()
    return data[user_id]