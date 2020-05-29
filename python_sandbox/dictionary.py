# Collection which is unordered, changeable and indexed

# Create dictionary
person = {"first_name": "Kako", "surname": "Bonf", "age": 34}

print(person, type(person))

# Using contructor
person2 = dict({"first": "First", "lastname": "Last"})
person3 = dict(first="First", lastname="Last")

print(person2, type(person2), person3, type(person3))

# Get value
print(person["first_name"])
print(person.get("first_name"))

# Add key-value
person["phone"] = "555-12011"

print(person)

# Get Dictionary keys
print(person.keys())

# Get Dictionary items
print(person.items())

# Copy dictionary
person_mock = person.copy()
person_mock["city"] = "San Paolo"

print(person_mock)

# Remove item'
del person["age"]
person.pop("phone")

print(person)

# Get Length
print(len(person))

# Clear
person.clear()

# List of dictionaries
people = [
    {"first_name": "Kako", "surname": "Bonf", "age": 34},
    {"first_name": "Kevin", "surname": "Doe", "age": 22},
]

print(people)
print(people[0]["surname"])
