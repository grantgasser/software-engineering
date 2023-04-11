import json

x = '{"name": "Bob", "age": 20, "city": "SF"}'

# convert from json to dict
bob = json.loads(x)
print(bob)

# convert from data to json
json.dumps({"name": "bob", "age": 20})
json.dumps(['apple', 'banana'])
json.dumps(32)
json.dumps(False)

# and so on...