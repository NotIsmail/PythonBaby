# Here we are gonna learn about functions the code is commented using multi line comment sign
"""
def Hello(name):
    print("Hello ,", name)


name = input("Enter your name:")
Hello(name)
"""

# There are ways where we can assign a default value to a function wherein there is a case where the value isn't passed or entered so the new code would be written below and the above line would be commented

"""
def Hello(name="World"):
    print("Hello,", name)


Hello()
name = input("Enter the name:")
Hello(name)

"""

# now we are gonna solve a problem for convenience of accessing functions from any part of the code sso what essessentially we are going to do is create main and we r gonna comment out the previous code too


def main():
    Hello()
    name = input("Enter your name:")
    Hello(name)


def Hello(name="World"):
    print("Hello,", name)


main()
