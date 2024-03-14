# now this program is a little course of tuple where we are gonna see it's properties (not in depth)
def main():
    student=get_student()
    print(f"{student[0]}'s favorite movie is {student[1]}")   # here it is accessed this way as it is a tuple and not a single value
    '''
    here is another method of accessing the same thing
    name,movie=get_student()
    print(f"{name}'s favorite movie is {movie}")
    '''
def get_student():
    name=input("Enter name:")
    movie=input("enter you're favorite movie:")
    #return (name,movie)   # == tuple ==here this is not returning two value but in reality it is a tuple
    return [name,movie]    # == list 


# here in tuple the issue  is it is immutable meaning the value connot changed after intializing so to fix it there is a very very basic and easy fix that is change it to list meaning (tho not shown in code) tuple = (..) list = [..] means change the return value bracket


if __name__=="__main__":
    main()