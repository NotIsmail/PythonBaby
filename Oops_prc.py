# this is actually program where i was trying to learn the python using harvard's CS50P but the issue is the code he provided isn't actually not working only god knows why so the thing is i would first read everything from harvard course and for better understanding i wil watch other videos 
'''
class Student:
    ...

def main():
    stu_data=get_student()
    print(f"{stu_data.name}'s favorite genre is {stu_data.genre} and is favorite movie is {stu_data.movie}")

def get_student():
    stu_data=Student()                                          # this is called attributes 
    stu_data.name=input("Enter your name:")
    stu_data.genre=input("Enter your favorite movie genre:")
    stu_data.movie=input("Enter your favorite movie:")
    return stu_data()

if __name__=="__main__":
    main()
'''
# Just another way to do it is it is not working to (T_T)


'''
class Student:
    ...

def main():
    stu_data=get_student()
    print(f"{stu_data.name}'s favorite genre is {stu_data.genre} and is favorite movie is {stu_data.movie}")

def get_student():                                          # this is called attributes 
    name=input("Enter your name:")
    genre=input("Enter your favorite movie genre:")
    movie=input("Enter your favorite movie:")
    Student=Student(name,genre,movie)
    return Student

if __name__=="__main__":
    main()

'''


# Another method 

# so in this lecture we have leanrt to raise exceptions where a user might make some errors in filling in details so for exapmle ..
# and another use of using the class is to give a detailed and complex if conditions for example a lost full of values which is true for the if block

class Student:
    def __init__(self,name,genre,movie) -> None:
        if not name:
            raise ValueError("Missing name")        # we r trying and setting up a condition where if name not entered = valueerror
        if not genre in ["romance","drama","action","biographhy","war","crime","fantasy","sci-fi","thriller"]:
            raise ValueError("wrong genre")
        self.name=name
        self.genre=genre
        self.movie=movie

def main():
    stu_data=get_student()
    print(f"{stu_data.name}'s favorite genre is {stu_data.genre} and is favorite movie is {stu_data.movie}")

def get_student():                                          # this is called attributes 
    name=input("Enter your name:")
    genre=input("Enter your favorite movie genre:")
    movie=input("Enter your favorite movie:")
    try:                                                    #here we use the try and except to as usual to handle exceptions and error
        return Student(name,genre,movie)
    except:
        print("Please enter your name")
if __name__=="__main__":
    main()