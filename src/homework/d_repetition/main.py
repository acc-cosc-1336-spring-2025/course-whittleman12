import repetition

def menu():
    print("""Homework 3 Menu
    1-Factorial
    2-Sum odd numbers
    3-Exit""")

def run_menu():
    menu()
    option = int(input("Select a menu option: "))
    handle_menu_option(option)

def handle_menu_option(option):
    if option == 1:
        num = int(input("Enter a number between 1 and 10: "))
        if 0 < num < 10:
            repetition.get_factorial(num) 
        else:
            print("You must enter a valid number")
        print("Do you want to exit?")
    elif option == 2:
        num = int(input("Enter a number between 1 and 99: "))
        if 0 < num < 100:
            repetition.sum_odd_numbers(num)
        else:
            print("You must enter a valid number")
        print("Do you want to exit?")
    elif option == 3:
        print("Do you want to exit?")
    else:
        print("Invalid option, please try again")

run_menu()