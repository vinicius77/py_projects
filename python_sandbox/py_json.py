import json

userJson = '{"first_name": "John", "last_name": "Bon", "age": 30}'

# Parse to Dictionary
user = json.loads(userJson)

print(user)
print(user["first_name"])

car = {"mark": "Ford", "year": 1979}

carJson = json.dumps(car)

print(carJson)
