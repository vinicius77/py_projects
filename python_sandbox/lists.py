# Collection ordered and changeable

number = [1, 2, 3, 4, 5]
fruits = ["Apple", "Banana", "Pear"]

# Using constructor
number2 = list((1, 3, 5, 7, 9))

print(number, number2)

# Get a value
print(fruits[1])  # Banana

# Get the length
print(len(fruits))

# Append to The List
fruits.append("Carambola")

# Remove
fruits.remove("Pear")

# Insert into position
fruits.insert(1, "Strawberries")

# Remove with pop
fruits.pop(len(fruits) - 1)

print(fruits)

# Sort
fruits.sort()

print(fruits)

# Reverse Sort
fruits.sort(reverse=True)

print(fruits)

# Reverse List
fruits.reverse()

# Change value
fruits[0] = "Blue Berries"

print(fruits)
