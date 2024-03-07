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

#if re.search(r"^.+@.+\.edu$", mail): # here we can many number of '@" signs and it will be considered valid to fixx this"

#if re.search(r"^[^@]+@[^@]+\.edu$",mail): # now we might do similar conditions like in this one for example only character things

#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",mail): # now here the condition is like it only accepts alphanumeric and @ and alphanumeric

# the above approach might seem a little cryptic as there is so many conditions included in that so to fix that (it is correct tho)

#the another small change that can be done is sometimes the user inputs email in uppercase which turns out as error to fix it 
# some emails have multiple dots then followed by domain and subdomian wwhich our code reacts to as error whereas the below fix made may help it
if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|in|net|org|)$",mail,re.IGNORECASE): # this \w accepts all kind of alphanumeric input and even the domain names can be chnaged using the ("name"|"name")

    print("valid")
else:
    print("invalid")

