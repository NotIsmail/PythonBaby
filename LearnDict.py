# now it is just little course where i use the dictionary and it's introductory function
def main():
    student = get_student()
    print(f"{student['name']}'s favorite club is {student['club']}")


def get_student():
    name = input("enter name:")
    club = input("enter club:")
    return {"name": name, "club": club}


if __name__ == "__main__":
    main()
