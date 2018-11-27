""" Catering Calculator

This program was an assignment for CP1200 (like CP1401/CP1404) in 2014
Lindsay Ward, 18/02/2014

Pseudocode:

COST_PER_HEAD = 10.0
CHILD_RATE = 0.6
PREMIUM_RATE = 1.25

function main()
    display welcome message
    display menu
    get choice
    while choice is not 'q'
        if choice is 'i'
            display instructions
        else if choice is 'c'
            call calculate_and_print_catering()
        else
            display invalid choice message
        display menu
        get choice
    print farewell message


function calculate_and_print_catering()
    get number_of_adults
    while number_of_adults is < 0
        display error message
        get number_of_adults
    get number_of_children
    while number_of_children < 0
        display error message
        get number_of_children
    get service_type
    while service_type is not 'b' and service_type is not 'p'
        display error message
        get service_type

    cost = number_of_adults * COST_PER_HEAD + number_of_children * COST_PER_HEAD * CHILD_RATE
    service_message = 'basic'
    if service_type is 'p'
        cost = cost * PREMIUM_RATE
        service_message = 'premium'
    if number_of_adults is 1
        adult_message = 'adult'
    else
        adult_message = 'adults'
    if number_of_children is 1
        child_message = 'child'
    else
        child_message = 'children'
    display cost, service_type, number_of_adults, adult_message, number_of_children, child_message, service_message

"""

COST_PER_HEAD = 10.0
CHILD_RATE = 0.6  # 60%
PREMIUM_RATE = 1.25
MENU = "\nMenu:\n(I)nstructions\n(C)alculate Catering\n(Q)uit"
INSTRUCTIONS = "Enter number of adults and children and choose a service type.\n\
Basic:   food only    = {:0.2f} per adult\n\
Premium: food & drink = {:0.2f} per adult\n\
Children are always {}% of the price of adults.".format(COST_PER_HEAD, COST_PER_HEAD * PREMIUM_RATE, CHILD_RATE * 100)


def main():
    """Catering Calculator program"""
    print("Welcome to the Great CP1200 Catering Calculator!")
    print("Written by Lindsay Ward, February 2014")

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "I":
            print(INSTRUCTIONS)
        elif choice == "C":
            calculate_and_print_catering()
        else:
            print("Invalid menu choice.")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you for using the Great CP1200 Catering Calculator.")


def calculate_and_print_catering():
    """Get details for catering job; calculate costs based on inputs and constant rates; print results """
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

    # calculate catering details
    cost = number_of_adults * COST_PER_HEAD + number_of_children * COST_PER_HEAD * CHILD_RATE
    service_message = "basic"
    if service_type == 'P':
        # multiply basic total cost by premium rate to get premium total
        cost *= PREMIUM_RATE
        service_message = "premium"

    # print results, after determining correct singular/plural words
    if number_of_adults == 1:
        adult_word = "adult"
    else:
        adult_word = "adults"
    if number_of_children == 1:
        child_word = "child"
    else:
        child_word = "children"
    print("\nThat will be ${:0.2f} for the {} service for {} {} and {} {}. Enjoy!".format(
        cost, service_message, number_of_adults, adult_word, number_of_children, child_word))


main()
