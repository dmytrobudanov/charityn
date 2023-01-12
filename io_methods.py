import csv
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname("C:/Users/Admin/Desktop/charity_navigator"))

def read_settings() -> json:
    with open(os.path.join(BASE_DIR,'settings.json'),'r') as file:
        settings = file.read()
    
    return json.loads(settings)

def write_to_csv(data: list,filename: str,delimiter: str = ';',dirname: str= 'out') -> None:
    with open(os.path.join(BASE_DIR,dirname,filename + '.csv'),'a+',encoding='utf-8',newline='') as handler:
        writer = csv.writer(handler,delimiter = delimiter)
        writer.writerow(data)

def read_from_json(json_path: str) -> json:
    with open(json_path, 'r',encoding='utf-8') as handler:
        json_data = json.load(handler)

    return json_data

def read_from_txt(filename: str,dirname: str = 'in') -> list:
    data = []

    with open(os.path.join(BASE_DIR,dirname,filename + '.txt'),'r', encoding='utf-8') as file:
        for line in file:
            data.append(line.replace('\n', ''))
    
    return data

def read_from_csv(filename: str, delimiter: str,dirname: str= 'in') -> list:
    data = []

    with open(os.path.join(BASE_DIR,dirname,filename + '.csv'),'r', newline ='',encoding='utf-8') as handler:
        reader = csv.reader(handler,delimiter=delimiter)
        for row in reader:
            data.append(row)

    return data
