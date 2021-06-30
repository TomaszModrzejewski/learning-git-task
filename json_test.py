import json

data = {"data": {

   "id": 1,
   "name": "Something",
   "colors": ["red", "blue"]
  }
}


print(type(data))
# <class 'dict'>

# zróbmy z tego JSON
data_as_json = json.dumps(data)
print(type(data_as_json))
# <class 'str'>
print(data_as_json)
# {"data": {"id": 1, "name": "Something", "colors": ["red", "blue"]}}

# zróbmy z JSON-a obiekt pythonowy
data_from_json = json.loads(data_as_json)
print(type(data_from_json))
# <class 'dict'>
print(data_from_json)
# {'data': {'id': 1, 'name': 'Something', 'colors': ['red', 'blue']}}