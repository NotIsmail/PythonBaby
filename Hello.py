print("Hello world!!")
Author_Name = "Ismail"
Author_Age = 18
print(f"Say Hello to {Author_Name} He is {Author_Age}")
Author_Likings, Author_Movies, Author_Games = "Gaming", "La la land", "GTA 5"
print(
    f"Your Author {Author_Name} Likes {Author_Likings} {Author_Movies} {Author_Games}"
)


User_Name = input("Enter your Name:").strip().capitalize().title()
User_Age = int(input("Enter your Age:"))
# A Method where we clear up the unecessary spaces and as well as capitalizing things


# User_Name = User_Name.strip()


# Now we see that wen we wrote the full name only the first word was capitalized so to fix these we use title which capitalize every word's first letter (the previous function is commented due to the problem as mentioned in the abpve comment )
# User_Name=User_Name.capitalize()


# User_Name = User_Name.title()

# There are certain ways where we can reduce the number of lines so unlike the upper two methods (which is commented out) we can write it this way

# User_Name=User_Name.strip().capitalize().title()

#there is another way to even reduce the lines of code and that is mapping back to the input line and the previous method is commented out

print(f"Hello User:{User_Name} your age is:{User_Age}")

# we are gonna look at another method to access the first and last name

first_name,last_name=User_Name.split(" ")
print(f"Hello {first_name}")