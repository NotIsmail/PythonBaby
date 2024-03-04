# The properties relating to thee house , we have seen  below that we have used some raise errors to tackle the errors made by users now there is a little logical things that comes around the raise we raised

"""
class details:
    def __init__(self, name, house) -> None:
        self.name = name
        self._house = house

    # Now as we see that while changing the things in the attribute with dot it changes the therefore to fix this  we actually set the required attrribute as setters and getters where setter is sets up the condition and comapring the changes to condition it fixes the changes or else discards it
    # getter is denoted using the @property now ( this is properties of classs wt we r discusin r included)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("missing name")
        self._name = name

    # getter
    @property
    def Home(self):
        return self._house

    # setter
    # is wheree the condition is set upp and implemented
    # REMEMBER THAT THE VARIABLE NAME HAS TO BE SET THE SAME AS GETTER EXAMPLE : getter=Home then setter=Home.setter
    @Home.setter
    def Home(self, house):
        if house not in ["gryffindor", "slytherin", "ravenclaw", "hefflepuff"]:
            raise ValueError("Invalid House")
        self._house = house


def main():
    stu_Res = stu_details()
    # details.house = "London"  # now as the attributes can be changed elsewhere with the dot operator now to overcome this we use
    print(f"{stu_Res.name} is in {stu_Res._house}")


def stu_details():
    Name = input("Name:")
    House = input("house:")
    return details(Name, House)


if __name__ == "__main__":
    main()
"""


"""
# now we are learning a program for class methods . this is just some random example

# now the commented codes are a normal way to access class elements and it's objects and everything no we are going to look at the class methods
import random


class Hat:
    # we r making houses a class variable
    houses = ["Gryffindor", "slytherin", "ravenclaw", "hufflepuff"]

    # now here we don't create any kind of object nor any instances therefor we directly access the class and it's data and variables through classmethods
    # here cls is a methods where we directly access the class variable inside like the same how self is used to access

    @classmethod
    def sort(cls, name):
        print(name, " is in ", random.choice(cls.houses))


Hat.sort("harry potter")
"""


# now taking the example that we started the oops concept  with
class Student:
    def __init__(self, name, house) -> None:
        self.name = name
        self.house = house

    def __str__(self) -> str:
        return f"{self.name} is in {self.house}"

    @classmethod
    def get(cls):
        name = input("Enter the name:")
        house = input("Enter the house:")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)

if __name__=="__main__":
    main()