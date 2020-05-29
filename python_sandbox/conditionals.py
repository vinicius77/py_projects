x = 44
y = 42

# Comparison
# if / elsif / else
if x > y:
    print(f"{x} is greater than {y}")
elif x < y:
    print(f"{x} is less than {y}")
else:
    print(f"{x} and {y} are equal")

# Nested if
if x > y:
    print(f"{x} is greater than {y}")
    if x < 50:
        print(f"{x} is less than 50")

# Logical operators (and, or, not )
# and
if x > y and x < 50:
    print(f"{x} is greater than {y} and is less than 50")

# or
if x == y or x > 5:
    print(f"We accept x: {x}")

# not
if not (type(x) == "str"):
    print(f"{x} is probably a number.")

# Membership operator (not, not in)

value = 5
not_in_list = 7
numbers = [1, 2, 3, 4, 5]

# in
print(value in numbers)

# not in
print(not_in_list not in numbers)

# is
print(value is not_in_list)

# is not
print(value is not not_in_list)
