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

"""

Name = input("Enter your name:")
file = open("Name.txt", "a")

# Now as the things were just getting appended and no newline was added we can chage it this way

file.write(f"{Name}\n")
file.close
"""

# Now we r going to study about readding the text  file

"""
with open("Name.txt", "r") as file:
    lines = file.readlines()
for i in lines:
    print("Hello,", i.rstrip())
"""

# Now we are going to sort the the list names using the with open thing

"""
Name=[]
with open("Name.txt") as file:     # we don't have to mention to the "r" as by default it is set to read mode
    for name in file:
        Name.append(name.rstrip())

for Names in sorted(Name,reverse=True):
    print(f"Hello {Names}")
"""

# Now we are going to look at accessing and printing a csv (Comma separated value) file
"""
with open("Name_List.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is a {row[1]}")
"""


# The above code actually being too cryptic too read as a reason we now change it too a little easier code to write
"""
Celebs=[]
with open("Name_List.csv") as file:
    for line in file:
        name, profession = line.strip().split(",")      #Here instead of naming a single variable then using the indexing for the code we cna directly use the python feature where we separate two variables and assign them their respective values
        Celebs.append(f"{name} is a {profession}")   # and as of here we changed it from indexing to the respective variable name

# We can even sort the names like below
for Name_sort in sorted(Celebs):
    print(Name_sort)
"""

# w instead of sorting the name in the english manner we can sort it in according to the names
"""
Celebs = []
with open("Name_List.csv") as file:
    for line in file:
        name, profession = line.strip().split(",")
        celeb = {"Name": name, "profession": profession}
        Celebs.append(celeb)

#def get_key(celeb):
    #return celeb["Name"]

# now we saw a way to take in the dictionary key and returning it's value here now we can use a keeyword where we can do it wihtout func.

for celeb in sorted(Celebs, key=lambda student:student["Name"]):
    print(f"{celeb['Name']} is in {celeb['profession']}")
"""

# now we r going to use the module named csv reader

"""
import csv

celebs = []
with open("Name_List.csv") as file:
    reader = csv.reader(file)
    for name, profession in reader:
        celebs.append({"name": name, "profession": profession})

    for celeb in sorted(celebs, key=lambda celeb: celeb["name"]):
        print(f"{celeb['name']} is in {celeb['profession']}")
"""


# Now we are going to look at the way where we use a function named csvdictreader which helps in accessing the key and values more easily
# Importance of csv is even when the data column is changed the things remain same
"""
import csv

celebs = []
with open("Name_List.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        celebs.append({"name": row["name"], "profession": row["profession"]})

    for celeb in sorted(celebs, key=lambda celeb: celeb["name"]):
        print(f"{celeb['name']}  is a {celeb['profession']}")
"""


# Now writing to a csv file
"""
import csv

name = input("Enter your name:")
professions = input("Enter your profeession:")
with open("Name_List.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, professions])
"""

import csv

profession = input("Enter your profession:")
name = input("Enter your name:")
with open("Name_List.csv", "a") as file:
    write = csv.DictWriter(file, fieldnames=["profession", "name"])
    write.writerow({"profession": profession, "name": name})
