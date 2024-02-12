from calc_Test import calc_Sq
import pytest


def main():
    test_Imp_Sq()


def test_Imp_Sq():
    # Now as we see there are horrendous error messages which  are difficult for user so let's put exceeptions
    """
    try:
        assert calc_Sq(2) == 4
    except AssertionError:
        print("2 sqaured ain't 4")
    try:
        assert calc_Sq(3) == 9
    except AssertionError:
        print("3 squared is not 9")
    """

    # as in the above program we used various try and except to fix errors but it is not efficient as there is too many lines of code therefore to fix this we use the package named pytest which does try except on its own

    # so as we know wt the issue is and how it reacts when a error is there we will now cheeck how it reacts for correct things

    assert calc_Sq(2) == 4
    assert calc_Sq(3) == 9


# So as we see we need to remember a very important point of always naming the testing functions and files with the word "test_"/"_test" in them and remember to use lowercase t in "test".


# Now we are going to check the use of the import library and to change it to TypeError


def Test_str():
    with pytest.raises(TypeError):
        calc_Sq("cat")


if __name__ == "__main__":
    main()
