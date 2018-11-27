"""
CP1404/CP5632 - Basic functions
Demonstrating various parameters, returns and the use of a main function
"""


def main():
    """Demo of simple program with functions."""
    lowest, highest = get_limits()
    print("lowest =", lowest, "highest =", highest)
    print_between(lowest, highest)


def get_limits():
    """Get minimum and maximum numbers (integer limits)."""
    minimum = int(input("Enter the minimum: "))
    maximum = int(input("Enter the maximum: "))
    return minimum, maximum


def print_between(start, end):
    """Print integers between start and end."""
    for i in range(start, end + 1):
        print(i, end=' ')


main()
