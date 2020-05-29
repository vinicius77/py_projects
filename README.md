## Python

Cover the basics of Python getting concepts from both CS50 and Brad Traversy Media Crash Courses.

Python was released in 1991, is heavily inspired by C as its syntax.
We will use Python 3 in the examples

## Syntax

### Variables

No type specifier
Declared by initialization only
Statements doesn't need with semicolons

### Conditionals

IF / ELSE
if y < 43 or z > == 15:
    #goes here
elif not coursenum == 51:
    #goes here

TERNARY OPERATOR
letters_only = True if input().isalpha() else False

LOOPS (WHILE AND FOR)
counter = 0
while counter < 100:
    print(counter)
    counter+= 1

for x in range(100):
print(x)

#starts from 0 til 100 (not inclusive) increasing by 2
for x in range(0, 100, 2):
    print(x)

### LISTS (Arrays)
nums = []
nums.append(5)

#inserts in the list position's 1 the value 6
nums.insert(1, 6)

#inserts in the list position's 2 the value 7
nums[len(nums):] = [7]

#creates a list with 500 elements
nums_2 = [x for x in range(500)]

nums_3 = list();

### Tuples
Ordered and immutable sets of data (The order matters)

List of tuples
presidents = [
    ("George Washington", 1789),
    ("John Adams", 1797),
    ("Thomas Jefferson", 1801),
    ("James Madison", 1809)
]

Iterating over Tuples
for pres, year in presidents:
    print("In {1}, {0} took office".format(pres,year))

### Dictionaries (Hash Table) key-value pairs
pizzas = {
    "cheese": 9,
    "pepperoni": 10,
    "vegetable": 11,
    "buffalo chicken": 12
}

pizzas["cheese"] = 8

if pizza["vegetables"] < 12:
    #do something

pizzas["bacon"] = 14

Iterating over dictionaries
for pie in pizzas:
    print(pie)

for pie, price in pizzas.items():
    print(price)

for pie, price in pizzas.items():
    print("A whole {} pizza costs ${}".format(pie, price))

## Variable Interpolation
print("A whole {} pizza costs ${}".format(pie, price))

print("A whole " + pie + " pizza costs $" + str(price))

#deprecated , avoid using this
print("A whole %s pizza costs $%2d" % (pie, price))

## Functions
def square(x):
    return x ** 2

## Objects
class Student():

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def changeID(self, id):
        self.id = id
    
    def print(self):
        print("{} - {}".format(self.name. self.id))

jane = Student("Jane", 10)
jane.print()
jane.changeID(11)
jane.print()

## Style
No more curly braces
No more semi-colon
Tabs and identation are essentials

## Including files (Modules)
import numpy as np

# Python Syntax
python your_program.py