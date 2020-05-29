# Collection which is ordered and unchangeable

# Creating tuples
fruits = ("Apples", "Pear", "Grapes")
fruits2 = tuple(("Apples", "Pear", "Grapes"))

print(fruits, fruits2)

# Single values needs trailing comma
fruits3 = ("Single",)
print(type(fruits3))

# Get value
print(fruits2[2])

# CANNOT change the value
# fruits2[1] = "Error"

# Get length
print(len(fruits2))

# Delete tuple
del fruits2

# SETS ===========
# A collection which is unordered and unindexed. (No duplicate values)

# Create a set
fruits_set = {"Apples", "Oranges", "Mango"}

# Check if in set
print("Apples" in fruits_set)

# Add to set
fruits_set.add("Watermellon")

# Don't duplicate values
fruits_set.add("Watermellon")

# Remove from set
fruits_set.remove("Mango")

# Clear set
fruits_set.clear()

# Delete set
del fruits_set  # NameError: name 'fruits_set' is not defined

print(fruits_set)
