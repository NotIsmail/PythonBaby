# This is just some random practice program
"""
name = []
for i in range(3):
    name.append(input("Enter your name:"))

for j in sorted(name):
    print(name)
"""

# Now's the real deal how to open aand write to file
# Now we encounter a issue where everytime we run things the previously written things are rewritten so we use append instead of write

Name = input("Enter your name:")
file = open("Name.txt", "a")

# Now as the things were just getting appended and no newline was added we can chage it this way

file.write(f"{Name}\n")
file.close
