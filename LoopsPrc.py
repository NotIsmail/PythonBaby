# Today we are going to to learn loop
"""
i = 3  # the condition can be i=1
while i != 0:  # the condition can also be i<=3
    print("Save me from the new changes please")
    i = i - 1  # so for the above commented conditions it can be changed to i=i+1


# Use of for loops and while loops
while True:
    n = int(input("Enter a amount:"))
    if n > 0:
        break

for i in range(n):
    print("Jaw and hair and career goals : peak")

"""
'''
# Use of lists in python
students = ["Harry", "Hermoine", "Ron"]

# Below is a way to acccess elements from the list using for loop


for student in students:
    print(student)
"""

# Below is another way to access it the same way



for i in range(len(students)):
    print(i + 1, students[i])       #here we have used to i+1 but we can use i too
'''
# Now we are going to take a look at how to use dictionary


"""
students = {
    "Harry": "Gryffindor",
    "Hermoine": "Gryffindor",
    "Ronald": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student, students[student], sep=" = ")
"""

# Now we are going to see a special code where we use dictionary in list and access multiple keywords and variables in single line

students = [
    {"Name": "Harry", "House": "Gryffindor", "Patronus": "Stag"},
    {"Name": "Hermoine", "House": "Gryffindor", "Patronus": "otter"},
    {"Name": "Ron", "House": "Gryffindor", "Patronus": "terrier"},
    {"Name": "Draco", "House": "Slytherin", "Patronus": None},
]
for student in students:
    print(student["Name"], student["House"], student["Patronus"], sep=" , ")


# This is am example for nested loops and printing a multi dimensional loops
def main():
    D_Square(3)


def D_Square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


main()
