# String Formats

name = "Kako"
age = 35

# Concatenate
print("Hello, I am " + " and I'm " + str(age) + " years old.")

# Arguments by position
print("My name is {name} and I am {age} years old".format(name=name, age=age))

# F-String (Python +3.6)
print(f"Hello, I am {name} and I am {age} years old.")

# String Methods
s = "hello python"

# Capitalize
print(s.capitalize())

# Swap Cases
print(s.swapcase())

# Uppercase
print(s.upper())

# Lowercase
print(s.lower())

# Get Length
print(len(s))

# Replace
print(s.replace("python", "developer"))

# Count the number of occurencies of the "sub"
sub = "y"
print(s.count(sub))

# Start with
print(s.startswith("hello"))

# Ends with
print(s.startswith("go"))

# Split into a list
print(s.split())

# Find position
print(s.find("p"))

# Is Alphanumeric
print(s.isalnum())

# Is Numeric
print(s.isnumeric())

# Is Alpha
print(s.isalpha())
