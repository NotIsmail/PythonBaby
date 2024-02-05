# Exception handling codes

"""
try:
    Number = int(input("Enter a number:"))
    print(f"The number you entered is {Number}")
except:
    print("I asked you to enter a number u mf")
"""
# now we r gonna look at a different case which haas a little things to do with the assignment operator


"""
try:
    x = int(
        input("Enter the number:")
    )  # we get name error cuz of the assingment won't get completed therefore to fix this
except:
    print("You entered the wrong number fool")
else:  # we use the else keyword which prints the error message we typed if error occurs or else give o/p
    print(f"The number u entered is  {x}")  # wen u run this we get name error
"""

# This code below shows us the use of loops in the exception handling where on error occurnces ur message is iterated
"""
while True:
    try:
        x = int(input("Enter the number:"))
    except:
        print("I made it clear that u need to enter a number")
    else:
        break

print(f"The number u entered is{x}")
"""

# Now i am going to use functions and potray the use of tyr and except


def main():
    x = Get_Int()
    print(f"The number is {x}")


# method 1 rather a very simple straightforward and most commonly used method

"""
def Get_Int():
    while True:
        try:
            x = int(input("Enter the number:"))
        except:
            print("I made it clear that u need to enter a number")
        else:
            break
    return x
"""

# Method 2 where it is just a little efficient code of by reducing the line of the codes

"""
def Get_Int():
    while True:
        try:
            x = int(input("Enter the number:"))
        except:
            print("I made it clear that u need to enter a number")
        else:
            return x
        # we r using return instead of the break cuz return - returns the value also and is a stronger than break statement in actually cutting out of the loop
"""

# Now we r using method 3 which even reduces the lines of codes and makes it efficient

'''
def Get_Int():
    while True:
        try:
            return int(
                input("Enter the number:")
            )  # from the above example we used return to directly reduce the conditional checking thing and making it direct
        except:
            print("I made it clear that u need to enter a number")
'''

# now wt we r sseeing is the convenience code that is instead of pointing out the error we can directly iterate the question loop with oout never letting the user or caller know this is done by using keyword called pass

def Get_Int():
    while True:
        try:
            return int(
                input("Enter the number:")
            )  # from the above example we used return to directly reduce the conditional checking thing and making it direct
        except ValueError:
            pass
main()