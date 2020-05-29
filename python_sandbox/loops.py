people = ["Clark", "Ralf", "Leona", "Heidern"]

# Simple for loop
for person in people:
    print(f"Person: {person}")

print("====================")

# Break
for person in people:
    if person == "Leona":
        break
    print(f"Person: {person}")

print("====================")

# Continue
for person in people:
    if person == "Clark":
        continue
    print(f"Person: {person}")

print("====================")
# Range
for i in range(len(people)):
    print(people[i])

for i in range(1, 10):
    print(f"Number {i}")

# While loop execute a set of statements as long as a condition is true
counter = 0
while counter < 11:
    if counter <= 1:
        print(f"{counter} beer")
        counter += 1
    else:
        print(f"{counter} beers")
        counter += 1
