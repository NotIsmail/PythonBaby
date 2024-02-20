class Student: ...


def main():
    student = Get_Name()
    print(f"{student.name} profession:{student.profession}")


def Get_Name():
    student = Student()
    student.name = input("Enter the name:")
    student.profession = input("Enter the profession:")
    return student


if __name__ == "__main__":
    main()
