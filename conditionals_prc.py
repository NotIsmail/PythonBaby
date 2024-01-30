# We are going to learn conditionals in python

"""
number1 = int(input("Enter your first number:"))
number2 = int(input("Enter your second number:"))
"""

# This is one way to work the other way is

"""
if number1>number2:
    print(f"{number1} is greater")
elif number2>number1:
    print(f"{number2} is greater")
"""

# The other way is

"""
if number1>number2 or number2>number1:
    print("The numbers are not equal")
else:
    print("The numbers are equal")    
"""

# A practice code


"""
score = int(input("Enter your score:"))
if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 80 and score <= 90:
    print("Grade B")
else:
    print("Grade F")
"""

# This is the program to indicate the modulo operator function
"""
number = int(input("Enter the number:"))
if number % 2 == 0:
    print("It is even")
else:
    print("It is odd")
"""

# Now working on match case same funcction as that of switch in other languages

name = input("Enter the name:")
match name:
    case "Ismail" | "John" | "Tommy":
        print(f"{name} plays GTA 5")
    case "Henry" | "Cilian" | "Timothee":
        print(f"{name} plays warhammer and RDR")
    case _:
        print(f"{name} plays Call Of Duty")
