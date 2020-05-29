# Create a function
def sayHello(name="Guest"):
    print(f"Hello {name}")


sayHello("Vin")
sayHello()

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total


result = getSum(4, 8)

print(result)

# Lambda Function is a small function which can take any number of arguments but can only have one expression (similar of arrow functions)
getMult = lambda num1, num2: num1 * num2

print(getMult(4, 7))
