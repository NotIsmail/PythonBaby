# hello therere we are now tackling a new type of error where we might tend to make errors while writing names like putting up the last name first and first name last or with extra whitespaces or with a comma so to fix that
import re

"""
name = input("Enter the name:").strip()  # here we are striping whitespaces with strip
matches = re.search(
    r"^(.+), *(.+)$", name
)  # now here we are using brackets to probably use the effect only on the given condition everything else is other than that ssame but here we used ", *" which removes extra white spaces with out resulting it in output
if matches:
    name = (
        matches.group(2) + " " + matches.group(1)
    )  # now here we use the groups"()" from above to call it certain number to interchnage ig the name is entered reversed and extra space i don't really know why
print(f"heloo,{name}")

"""

"""
name = input("Enter the name:").strip() 
if matches := re.search(r"^(.+), *(.+)$", name) this := is a walruus operator where in this context we are assigning matches here with the search operator and then we are checking the condition therefore it helps us to do two or many things with this operator
    name = matches.group(2) + " " + matches.group(1) 
print(f"heloo,{name}")
"""


# now we are going to learn about re.sub fucntion which as an example imagine you are entering you're twitter username and as a convention we copy the url of our username and we paste it so now with the help of the below program we can just extract the username from the url using re.sub
"""
url = input("Enter the url:").strip()
username = re.sub(r"https://twitter.com/", "", url)
print(username)
"""

# now the above program might accomplish the job that we require but we might need more exclusivity so like imagine a user might eenter https or htttp or www. or sometimes skip all of em so to fix these we just make use of the special characters by the re modlue and make it more flexible like in the code below

# 1 . tackling the https or http thing : we can do either (http|https) or we can even do (https?)
# 2. tackling no protocol at all : we can do it as follows (https?:\\)?
# 3 . tackling www. instead of http or https : we can do it (https?:\\)?(www\.)?
"""
url = input("Enter the url:").strip()
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(username)
"""
# now there might be some scenarios where user might completely unrelated url and from our above code which might start misbehaving so to fix it
url = input("Enter the url:").strip()
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"username:", matches.group(1))
