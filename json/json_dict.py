import json

"""
References
==========
http://docs.python-guide.org/en/latest/scenarios/json/
"""
# json string
json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

# parse json into a dictionary
json_dict = json.loads(json_string)
print(type(json_dict))
print(json_dict)

# read in json_dict and output into a string
json_string = json.dumps(json_dict)
print(type(json_string))
print(json_string)
