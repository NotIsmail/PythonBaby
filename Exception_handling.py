# Exception handling codes

"""
try:
    Number = int(input("Enter a number:"))
    print(f"The number you entered is {Number}")
except:
    print("I asked you to enter a number u mf")
"""
# now we r gonna look at a different case which haas a little things to do with the assignment operator

try:
    x = int(
        input("Enter the number:")
    )  # we get name error cuz of the assingment won't get completed therefore to fix this
except:
    print("You entered the wrong number fool")
else:  # we use the else keyword which prints the error message we typed if error occurs or else give o/p
    print(f"The number u entered is {x}")  # wen u run this we get name error
