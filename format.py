# hello therere we are now tackling a new type of error where we might tend to make errors while writing names like putting up the last name first and first name last or with extra whitespaces or with a comma so to fix that
import re

name = input("Enter the name:").strip() #here we are striping whitespaces with strip
matches = re.search(r"^(.+), *(.+)$", name) # now here we are using brackets to probably use the effect only on the given condition everything else is other than that ssame but here we used ", *" which removes extra white spaces with out resulting it in output
if matches:
    name = matches.group(2) + " " + matches.group(1) # now here we use the groups"()" from above to call it certain number to interchnage ig the name is entered reversed and extra space i don't really know why 
print(f"heloo,{name}")
'''
name = input("Enter the name:").strip() 
if matches := re.search(r"^(.+), *(.+)$", name) this := is a walruus operator where in this context we are assigning matches here with the search operator and then we are checking the condition therefore it helps us to do two or many things with this operator
    name = matches.group(2) + " " + matches.group(1) 
print(f"heloo,{name}")
'''