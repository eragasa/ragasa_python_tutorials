import json
from collections import OrderedDict
# json string
d = OrderedDict([
    ("first_name","Guido"),
    ("last_name","Rossum")
])

# parse the OrderedDict into a JSON string
json_str = json.dumps(d)
print(type(json_str)==str)
print("json_str:{}".format(json_str))

# parse JSON string into an OrderedDict
s = '{"first_name": "Guido", "last_name":"Rossum"}'
json_dict = OrderedDict(json.loads(s))
print(type(json_dict)==OrderedDict)
print(json_dict)
