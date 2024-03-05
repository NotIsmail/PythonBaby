# Here an example of a random condition that is passed done in a normal method
'''
mail=input("Enter your E-mail:")
if mail=="@":
    print("valid E-mail")
else:
    print("Invalid")
'''

# a little more sophisticated method would be like
# mail=input("Enter your E-mail:") sorry i forgot what was i supposed to write

# using the re (regular expressions) module 
import re
mail=input("Enter your E-mail:")

#if re.search("@",mail):  # this line would  just check the given string or wtver just like the above so to fix this we might try

#if re.search(".*@.*",mail): # this line tho won't fix the acctual issue offc it fixes the issue for the sake but not completely

#if re.search(".+@.+",mail): # this ine can further be modified for a desired requirement of domain name . see below 

#if re.search(r".+@.+\.edu",mail):  # we used "r" which means a raw string that allows us to use \n without python interfering with actual \n 

# now in the above code we could've written a whole ass sentence and it would've considered value as there is '.' and '+' value which includes value
# therefore it can be fixed as follows
# here this just sees that wtever text is in '^' and '$' is matched and then returned true
if re.search(r"^.+@.+\.edu$", mail): 
    print("valid")
else:
    print("invalid")

