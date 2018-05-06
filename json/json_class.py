import json
from collections import OrderedDict

class Person(object):
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self):
        d = OrderedDict()
        d['first_name'] = self.first_name
        d['last_name'] = self.last_name

        return json.dumps(d)

    def from_json(s):
        d = json.loads(s)
        o = Person(
            first_name = d['first_name'],
            last_name = d['last_name']
        )
        return o

# json string
s = '{"first_name": "Guido", "last_name":"Rossum"}'
d = OrderedDict([
    ("first_name","Guido"),
    ("last_name","Rossum")
])

person = Person(
    first_name = d["first_name"],
    last_name = d["last_name"]
)

print(80*"=")
print("Person.__init__")
print(80*'-')
print("person.__dict__")
print("type(person.__dict__)",type(person.__dict__))
print(person.__dict__)
print("person.to_json")
print(person.to_json())

print(80*"=")
print("Person.from_json")
print(80*'-')
print("person.from_json(s)")
person = Person.from_json(s)
print("person.__dict__")
print("type(person.__dict__",type(person.__dict__))
print(person.__dict__)
print("person.to_json")
print(person.to_json())
