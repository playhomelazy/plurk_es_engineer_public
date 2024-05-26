import os
import json

def check_member(id):
    database = os.listdir('./member')
    if str(id)+'.json' not in database:
        new_data(id)
    return True

def new_data(id):
    data = {
        'id':id,
        'exp':10,
        '3_stars': [0]*49,
        '4_stars': [0]*49,
        '5_stars': [0]*49,
        'fans':0
    }
    data = json.dumps(data, ensure_ascii=False)
    with open('./member/' + str(id) + '.json','w',encoding="utf-8") as write_data:
        write_data.write(data)
