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

    def __str__(self):
        '''return "a person"'''  #so this thing kind of returns a value wen no data is entered and not a cryptic memory location we got some issue the required output wasn't recieved so the below value works as much as the print statement but also returns in redable form not like in the print statement
        return f"{self.name} likes {self.genre} likes {self.movie}"


def main():
    stu_data=get_student()
    print(stu_data)       # the code in this print statement kind of accessed the obj and then printed it but now to reduc the code we did this and when we run this code we get a cryptic output stating it's location in the computer's memory so to fix this we kinda use the above def __str__ method

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