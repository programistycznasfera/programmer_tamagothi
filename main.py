import random
import time
import string
import os
import colorama
import pymsgbox
import json
from pymsgbox import *
# Player Stats
Health = 100
Sanity = 100
Money = 100
Hunger = 100
Name = input("Input your name:")
def show_help():
    """Funkcja wyświetlająca pomoc."""
    print("Avaible activities:")
    print("1:Programming - Increase money and  sanity")
    print("2:Go to a psychologist - Increases mental health by 25%")
    print("3:Eat a fast-food - Increase hunger level and decrease mental health by 2%")
    print("4:Show statistics")
    print("5:Save")
    print("6:Load")
def main():
    show_help()  # Wyświetlenie pomocy na początku
    while True:
        user_input = input("Enter activity: ").strip().lower()  # Pobieranie komendy od użytkownika

        if user_input == "1":
            print("Make a software Earned a 70$")
            Money + 70
        elif user_input == "2":
            print("You go to pshychologist and mental health increase by 25$ and lose 13%")
            Money - 25
        elif user_input == "3":
            print("You go to MCDonald")
            print("You lose 25$ bucks")
            print("Decrease 2% of mental health")
            Money - 25
            Sanity - 2
        elif user_input == "4":
            print("----------------")
            print(f"Sanity:{Sanity}%")
            print(f"Money:{Money}$")
            print(f"Hunger:{Hunger}%")
        elif user_input == "5":
            save_variables_to_json
        elif user_input == "6":
            load_variables_from_json
        else:
            print(f"{Name} doesn't know")
        if Hunger == 0:
            print("You lose...")

        break
    if Money == 0:
        print("You are bankrupt")
        alert(text='You are bankrupt', title=f'{Name} is homeless', button='OK')
    if Sanity == 0:
        print("You're crazy")
        alert(text='You have a mental breakdown', title=f'{Name} haves a mental breakdown', button='OK')

def save_variables_to_json(variables_dict, filename):
    """Funkcja zapisująca zmienne do pliku JSON."""
    with open(filename, 'w') as file:
        json.dump(variables_dict, file)

def load_variables_from_json(filename):
    """Funkcja wczytująca zmienne z pliku JSON."""
    with open(filename, 'r') as file:
        variables_dict = json.load(file)
    return variables_dict


# Zapis zmiennych do pliku JSON
variables_dict = {
    "Hunger": Hunger,
    "Name": Name,
    "Sanity": Sanity,
     "Money": Money,
}
save_variables_to_json(variables_dict, "save.json")
print("Zmienne zostały zapisane do pliku 'save.json'.")

# Wczytanie zmiennych z pliku JSON
loaded_variables = load_variables_from_json("save.json")
print("Wczytane zmienne z pliku JSON:")
print(loaded_variables)
if __name__ == "__main__":
    main()
