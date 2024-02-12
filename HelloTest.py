def main():
    name = input("Enter your name:")
    output = hello(name)
    print(output)


def hello(to="World"):
    return f"Hello {to}"


if __name__ == "__main__":
    main()
