from calcTest import calc_Sq


def main():
    Imp_Sq()


def Imp_Sq():
    # Now as we see there are horrendous error messages which  are difficult for user so let's put exceeptions
    try:
        assert calc_Sq(2) == 4
    except AssertionError:
        print("2 sqaured ain't 4")
    try:
        assert calc_Sq(3) == 9
    except AssertionError:
        print("3 squared is not 9")


if __name__ == "__main__":
    main()
