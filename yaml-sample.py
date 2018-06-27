#!/usr/bin/python3.6
import yaml
#import json
data = {'Name': 'Nikhil','age' : 20,'handles': {'facebook': 'sddd12','github':'testing','youtube':'Pythontic'},
        'languages': {'markup': ['HTML','XML','AIML'],'programming': ['C','C++','Python','javascript']}}
#print(data)
print("Data in the YAML Form\n")
print(yaml.dump(data, default_flow_style=False))
print("Data in the Data Structure Form\n")
print(yaml.load(data))
