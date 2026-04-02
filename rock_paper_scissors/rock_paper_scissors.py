import random
import os

user_name = input("Enter your name: > ")
print(f"Hello, {user_name}")

user_rating = 0
if os.path.exists("rating.txt"):
    with open("rating.txt", "r") as file:
        for line in file:
            name, score = line.split()
            if name == user_name:
                user_rating = int(score)

print("Enter a set of game symbols to be used in this game:")
options_input = input("> ")

if options_input == "":
    options = ["rock", "paper", "scissors"]
else:
    options = options_input.split(",")

print("Okay, let's start")

while True:
    user_choice = input("> ")

    if user_choice == "!exit":
        print("Bye!")
        break
    
    if user_choice == "!rating":
        print(f"Your rating: {user_rating}")
        continue

    if user_choice not in options:
        print("Invalid input")
        continue

    computer_choice = random.choice(options)
    
    if user_choice == computer_choice:
        print(f"There is a draw ({computer_choice})")
        user_rating += 50
    else:
        idx = options.index(user_choice)
        reordered_options = options[idx + 1:] + options[:idx]
        half = len(reordered_options) // 2
        defeated_by_user = reordered_options[half:]

        if computer_choice in defeated_by_user:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_rating += 100
        else:
            print(f"Sorry, but the computer chose {computer_choice}")
