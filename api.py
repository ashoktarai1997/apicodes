# json file working
import json

from DataDriver.json_reader import json_reader

courese = '{"name":"ashok","lastname":"tarai","language":["odia","hindi","english"]}'

dict_courses = json.loads(courese)
print(type(dict_courses))
print(dict_courses["language"])

print(dict_courses["language"][2])

with open("titanic.json","r") as file1:
    json_reader = file1.read()
    json_loads = json.loads(json_reader)
    print(type(json_reader))
    print(json_loads)

import json
with open("titanic.json", "r") as file1:
    data = json.load(file1)  # directly load JSON
    print(type(data))
    print(data)
import json

import json

with open("titanic.json", "r") as file:
    data = [json.loads(line) for line in file]

with open("titanic_array.json", "w") as outfile:
    json.dump(data, outfile, indent=2)

    print(data)


import json

json_data = {
    "id": 1,
    "name": "ashok",
    "salary": 7900,
    "age": 27
}

with open("ashok.json", "w") as file2:
    dict_convert_json = json.dumps(json_data)
    json_writer = file2.write(dict_convert_json)
# csv files
import csv

with open("Data1.csv") as file:
    csv_reader = csv.reader(file)
    for i in csv_reader:
        for j in i:
            print(j,end='')
    # print()

import json
with open('ashok.json') as f:
    data = json.load(f)
    print("this is very personal data",data)
    print(type(data))
    print(data ["course"][1]['title'])
    print(data["dashboard"])
    print(data['dashboard']['website'])



import json
with open('ashok.json') as f:
    data = json.load(f)
    print(data['course'][1]['title'])







