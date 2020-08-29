# Python

Cover the basics of Python getting concepts from both CS50 and Brad Traversy Media Crash Courses.

Python was released in 1991, is heavily inspired by C as its syntax.
We will use Python 3 in the examples

## Syntax

### Variables

No type specifier
Declared by initialization only
Statements doesn't need with semicolons

### Conditionals

#### IF / ELSE
```python
if y < 43 or z > == 15:
    #goes here
elif not coursenum == 51:
    #goes here
else:
    #goes here
```

#### TERNARY OPERATOR
```python
letters_only = True if input().isalpha() else False
```

### LOOPS (WHILE AND FOR)
```python
counter = 0
while counter < 100:
    print(counter)
    counter+= 1

for x in range(100):
print(x)

#starts from 0 til 100 (not inclusive) increasing by 2
for x in range(0, 100, 2):
    print(x)
```

### LISTS (Arrays)
```python
nums = []
nums.append(5)


#inserts in the list position's 1 the value 6
nums.insert(1, 6)

#inserts in the list position's 2 the value 7
nums[len(nums):] = [7]

#creates a list with 500 elements
nums_2 = [x for x in range(500)]

nums_3 = list()

# extending a list
list_name = ["ele1", "ele2"]
list_name.extend(["ele2", "ele3"]) 
print(list_name)
# ['ele1', 'ele2', 'ele2', 'ele3']

# Fetching the first two elements
list_name[:2]

# Fetching from the fourth element until the end of the list
list_name[4:]

# Fetching an element by its key
list_name.index("ele2") # returns the index 1

# sorting a list
list_name.sort(reverse = True) # reminds that sort does not return the sorted list; rather, it sorts the list in place.

# creating lists with range function
range_list = range(10) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range_list_2 = range(3,7) #[3, 4, 5, 6]
range_list_3 = range(1, 10, 2) #[1, 3, 5, 7, 9]

for number in range_list:
	print(number)

# or

for num in range(len(range_list):
	print(range_list[num])
```

### Enumerate
```python

### Another Example Which Can Be Replaced By The Enumerate Function

a_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for i in range(len(a_list)):
    print('The value at position {} is {}.'.format(i, a_list[i]))

for i, val in enumerate(a_list):
    print('The value at position {} is {}.'.format(i, val))
```

### Tuples
Ordered and immutable sets of data (The order matters)

#### Tuples Assignment
```
x = (40, 41, 42)

a, b, c = 1, 2 ,3

(age, years) = "8,17".split(",")

```

#### List of tuples
```python
presidents = [
    ("George Washington", 1789),
    ("John Adams", 1797),
    ("Thomas Jefferson", 1801),
    ("James Madison", 1809)
]
```

#### Iterating over Tuples
```python
for pres, year in presidents:
    print("In {1}, {0} took office".format(pres,year))
```

#### Example of a function a tuple

```
def square(x):
	AREA = x ** 2
	PERIMETER = 4 * x
	print(f"Perimeter and area of a square {PERIMETER} {AREA}.")

	return (PERIMETER ,AREA)
``` 

### Dictionaries (Hash Table) key-value pairs
```python
pizzas = {
    "cheese": 9,
    "pepperoni": 10,
    "vegetable": 11,
    "buffalo chicken": 12
}

people = { "name": "John Doe"}

pizzas["cheese"] = 8

if pizza["vegetables"] < 12:
    #do something

pizzas["bacon"] = 14
```

#### Iterating over dictionaries
```python
for pie in pizzas:
    print(pie)

for pie, price in pizzas.items():
    print(price)

for pie, price in pizzas.items():
    print("A whole {} pizza costs ${}".format(pie, price))
```

```
# Calculates money spent in a supermarket list
prices = {
	"spaghetti": 4,
    "lasagna": 3,
    "hamburger": 2
}

quantity = {
	"spaghetti": 6,
    "lasagna": 4,
    "hamburger": 3
}
 
money_spent = 0
 
for key in prices:
     money_spent += (prices[key] * quantity[key])

print(money_spent)
```

### Variable Interpolation
```python
print("A whole {} pizza costs ${}".format(pie, price))

print("A whole " + pie + " pizza costs $" + str(price))

#Deprecated! avoid using this
print("A whole %s pizza costs $%2d" % (pie, price))
```

### Functions
```python
def square(x):
    return x ** 2
```

### Objects
```python
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
```

### Style
* No more curly braces
* No more semi-colon
* Tabs and identation are essentials

### Including files (Importing Modules)
```python
import numpy as np

import math # math.sqrt(25)
from math import sqrt # sqrt(16)
from math import sqrt as s # s(4)
import math as m # m.sqrt(36)
from math import * #sqrt(81)

```

### help with modules
```python

help(math)

help(math.sqrt)
```

### Python Syntax
```python
python3 your_program.py
```

### [FLASK PYTHON BASED FRAMEWORK](https://linuxize.com/post/how-to-install-flask-on-ubuntu-18-04/)
```
sudo apt install python3-venv
cd /home/kako77sub
python3 -m venv venv
source venv/bin/activate
pip install Flask
python -m flask --version
```
```python
#~/py_projects/CS50/server/application.py
```
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

```

```
cd /home/kako77sub/Desktop/py_projects/CS50/server/
export FLASK_APP=application.py
flask run
```
### Deactivating the Virtual Environment
```
deactivate
```

PS.: MATH 3e5 == 3 * 10 ^ 5
