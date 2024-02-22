# we are noww seeing the use of classes which is useful for oop in python

# now we r using the other method of using the classes


class Student:
    def __init__(self, name, profession) -> None:
        # now we are using the if condition to tackle the situation where there is no name entered
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.profession = profession


def main():
    student = Get_Name()
    print(f"{student.name}  profession:{student.profession}")


def Get_Name():
    name = input("Enter the name:")
    profession = input("Enter the profession:")
    student = Student(name, profession)
    return student


if __name__ == "__main__":
    main()
