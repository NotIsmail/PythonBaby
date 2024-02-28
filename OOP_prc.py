# we are noww seeing the use of classes which is useful for oop in python

# now we r using the other method of using the classes


class Student:
    def __init__(self, name, profession, game) -> None:
        # now we are using the if condition to tackle the situation where there is no name entered
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.profession = profession
        self.game = game

    # we r writing this ffunction with cuz when we directly print the object it prints it'ss memory location therefore we r using this

    def __str__(self) -> str:
        return f"{self.name} is a {self.profession}"

    # here we can edit whatever message we want to writee as it is being called and the self is it's reference code

    def Game(self):
        if self.game == "GTA 5":
            return "❤️"
        else:
            return "👍"


def main():
    student = Get_Name()
    # print(f"{student.name}  profession:{student.profession}")
    print("Users fav game")
    print(student.Game())


def Get_Name():
    name = input("Enter the name:")
    profession = input("Enter the profession:")
    game = input("Your fav game:")
    student = Student(name, profession, game)
    return student


if __name__ == "__main__":
    main()
