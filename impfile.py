def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"Hello {name}")


def goodbye(name):
    print(f"Goodbye {name}")


# As we see we have a little issue where whole of the main function gets called and the helllo goodbye and every function is called and not our directedd function therefore to fix this

if __name__ == "__main__":
    main()
