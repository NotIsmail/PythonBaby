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