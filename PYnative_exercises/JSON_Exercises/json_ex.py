"""
ex1: Convert the following dictionary into JSON format
"""
# import json

# data = {"key1" : "value1", "key2" : "value2"}

# json_data = json.dumps(data)
# print(json_data)

"""
ex2: Access the value of key2 from the following JSON
"""
# import json
# sample_Json = """{"key1": "value1", "key2": "value2"}"""
# # write code to print the value of key2

# data = json.loads(sample_Json)
#print(data["key2"])

"""
PrettyPrint following JSON data with indent level 2 and key-value separators should be (",", " = ").

expected output:
{
  "key1" = "value2",
  "key2" = "value2",
  "key3" = "value3"
}
"""
# import json

# sampleJson = {"key1": "value1", "key2": "value2"}

# pretty_printed_json = json.dumps(sampleJson, indent=2, separators=(",","="))
# print(pretty_printed_json)

"""
Exercise 5: Access the nested key 'salary' from the following JSON
"""
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# write code to print the value of salary
# data = json.loads(sampleJson)
# print(data["company"]["employee"]["payble"]['salary'])  # output: 7000

"""
Exercise 6: Convert the following Vehicle Object into JSON

"""
import json
from json import JSONEncoder

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
#convert to json
jsonData = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
print(jsonData)
        