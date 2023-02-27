import csv
from datetime import datetime
import os

from decorator import Olives, Mushrooms, GoatCheese, Meat, Onions, Corn
from pizza import ClassicPizza, MargheritaPizza, TurkPizza, DominosPizza


def main():
    print("Welcome to Pizza Shop!")
    print("Please choose a pizza and sauce from the menu:")

    # Read menu from the file
    with open("Menu.txt", "r") as f:
        menu = f.read()
        print(menu)

    pizza_choices = {
        '1': ClassicPizza(),
        '2': MargheritaPizza(),
        '3': TurkPizza(),
        '4': DominosPizza()
    }

    sauce_choices = {
        '11': Olives,
        '12': Mushrooms,
        '13': GoatCheese,
        '14': Meat,
        '15': Onions,
        '16': Corn
    }

    pizza_choice = input("Choose a pizza (1-4): ")
    if pizza_choice not in pizza_choices:
        print("Invalid pizza choice.")
        return

    pizza = pizza_choices[pizza_choice]

    selected_sauces = []
    while True:
        sauce_choice = input("Choose a sauce (11-16), or 'done' if you're finished: ")
        if sauce_choice == 'done':
            break
        if sauce_choice not in sauce_choices:
            print("Invalid sauce choice.")
            continue

        sauce = sauce_choices[sauce_choice]
        pizza = sauce(pizza)
        # Check if sauce_choice is already in selected_sauces
        if sauce.__name__ not in selected_sauces:
            selected_sauces.append(sauce.__name__)
        else:
            print("You have already selected this sauce.")

    # Get total cost of pizza with sauce
    total_cost = pizza.get_cost()
    # Clearing the Screen
    os.system('cls')
    # Print order summary and ask for confirmation
    print("\nSelected pizza: " + pizza.__class__.__name__)
    print("Selected sauces: " + ', '.join(selected_sauces))
    print("\nTotal cost: $" + str(total_cost))

    while True:
        confirmation = input("\nDo you confirm your order? (yes/no): ")
        if confirmation.lower() == 'yes':
            break
        elif confirmation.lower() == 'no':
            print("Order cancelled.")
            return
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")

    # Get user information
    name = input("Enter your name: ")
    id_num = input("Enter your ID number: ")
    credit_card_num = input("Enter your credit card number: ")
    credit_card_password = input("Enter your credit card password: ")

    # Add order to database
    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y %H:%M:%S")
    with open("Orders_Database.csv", mode="a") as database:
        writer = csv.writer(database)
        writer.writerow(
            [name, id_num, credit_card_num, pizza.get_description(), ', '.join(selected_sauces),
             current_time, credit_card_password, total_cost])

    print("\nOrder placed successfully!")


if __name__ == '__main__':
    main()
