"""
This program was originally the CP1200 (Programming 1) Assignment 1 from 2014
Catering Calculator
Lindsay Ward
Created 18/02/2014, Updated 2026

Pseudocode:

COST_PER_HEAD = 10.0
CHILD_RATE = 0.6
PREMIUM_RATE = 1.25

function main()
    print welcome message
    print menu
    get choice
    while choice != 'q'
        if choice == 'i'
            print instructions
        else if choice == 'c'
            call process_catering()
        else
            print invalid choice message
        print menu
        get choice
    print farewell message


function process_catering()
    get number_of_adults
    while number_of_adults < 0
        print error message
        get number_of_adults
    get number_of_children
    while number_of_children < 0
        print error message
        get number_of_children
    get service_type
    while service_type != 'b' and service_type != 'p'
        print error message
        get service_type

    cost = number_of_adults * COST_PER_HEAD + number_of_children * COST_PER_HEAD * CHILD_RATE
    service_message = 'basic'
    if service_type == 'p'
        cost = cost * PREMIUM_RATE
        service_message = 'premium'
    if number_of_adults == 1
        adult_message = 'adult'
    else
        adult_message = 'adults'
    if number_of_children == 1
        child_message = 'child'
    else
        child_message = 'children'
    print cost, service_type, number_of_adults, adult_message, number_of_children, child_message, service_message

"""

COST_PER_HEAD = 10.0
CHILD_RATE = 0.6  # 60%
PREMIUM_RATE = 1.25

MENU = "\nMenu:\n(I)nstructions\n(C)alculate Catering\n(Q)uit"
INSTRUCTIONS = f"Enter number of adults and children and choose a service type.\n\
Basic:   food only    = ${COST_PER_HEAD:0.2f} per adult\n\
Premium: food & drink = ${COST_PER_HEAD * PREMIUM_RATE:0.2f} per adult\n\
Children are always {CHILD_RATE * 100}% of the price of adults."


def main():
    """Catering calculator demo program."""
    print("Welcome to the Great CP1200 Catering Calculator!")
    print("Written by Lindsay Ward, 2014-2026")

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "I":
            print(INSTRUCTIONS)
        elif choice == "C":
            process_catering()
        else:
            print("Invalid menu choice.")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you for using the Great CP1200 Catering Calculator.")


def process_catering():
    """Get details for catering job; calculate costs based on inputs and constant rates; print results."""
    number_of_adults = int(input("Please enter the number of adults: "))
    while number_of_adults < 0:
        print("Error. Please enter a number >= 0")
        number_of_adults = int(input("Please enter the number of adults: "))

    number_of_children = int(input("Please enter the number of children: "))
    while number_of_children < 0:
        print("Error. Please enter a number >= 0")
        number_of_children = int(input("Please enter the number of children: "))

    service_type = input("Would you like (B)asic or (P)remium service?: ").upper()
    while service_type not in ('B', 'P'):
        print("Error. Please enter b or p")
        service_type = input("Would you like (B)asic or (P)remium service?: ").upper()

    # Calculate catering cost
    cost = number_of_adults * COST_PER_HEAD + number_of_children * COST_PER_HEAD * CHILD_RATE
    service_message = "basic"
    if service_type == 'P':
        # Multiply basic total cost by premium rate to get premium total
        cost *= PREMIUM_RATE
        service_message = "premium"

    # Print results using appropriate singular/plural words
    if number_of_adults == 1:
        adult_word = "adult"
    else:
        adult_word = "adults"
    if number_of_children == 1:
        child_word = "child"
    else:
        child_word = "children"
    print()
    print(
        f"That will be ${cost:.2f} for the {service_message} service for {number_of_adults} {adult_word} and {number_of_children} {child_word}. Enjoy!")


main()
