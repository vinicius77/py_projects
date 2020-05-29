# Create a class


class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    # Method
    def greeting(self):
        return f"My name is {self.name} and I'm {self.age} years old"

    def has_bday(self):
        self.age += 1


# Init User Object
user = User("Vini", "vinicius@gmail.com", 35)

print(type(user))
print(user.name)
print(user.greeting())
print(user.age)
user.has_bday()
print(user.age)

# Extend Class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    # Overwrite greetinf function
    def greeting(self):
        return f"My name is {self.name} and I'm {self.age} years old and my balance is {self.balance}"


janet = Customer("Janet", "janet@yahoo.com", 44)
janet.set_balance(33)
print(janet.greeting())
