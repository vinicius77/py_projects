# Open a file

myFile = open("myfile.txt", "w")

# Get some info
print("Name: ", myFile.name)
print("Is closed?: ", myFile.closed)
print("Opening Mode: ", myFile.mode)

# Write to File
myFile.write("Python ")
myFile.write("Javascript")
myFile.close()

# Append File
myFile = open("myfile.txt", "a")
myFile.write("and Node.js")
myFile.close()

# Read From File
myFile = open("myfile.txt", "r+")
text = myFile.read(100)
print(text)
