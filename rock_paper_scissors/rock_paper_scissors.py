import random
import os

user_name = input("Enter your name: ")
print(f"Hello, {user_name}")

user_rating = 0
if os.path.exists("rating.txt"):
    with open("rating.txt", "r", encoding="utf-8") as file:
        for line in file:
            data = line.split()
            if data[0] == user_name:
                user_rating = int(data[1])

custom_options = input().strip()
if not custom_options:
    game_options = ["rock", "paper", "scissors"]
else:
    game_options = custom_options.split(",")

print("Okay, let's start")

while True:
    user_choice = input()

    if user_choice == "!exit":
        print("Bye!")
        break

    if user_choice == "!rating":
        print(f"Your rating: {user_rating}")
        continue

    if user_choice not in game_options:
        print("Invalid input")
        continue

    comp_choice = random.choice(game_options)

    if user_choice == comp_choice:
        print(f"There is a draw ({comp_choice})")
        user_rating += 50
    else:
        index = game_options.index(user_choice)
        reordered = game_options[index + 1:] + game_options[:index]
        
        half = len(reordered) // 2
        weak_against = reordered[:half]
        
        if comp_choice in weak_against:
            print(f"Sorry, but the computer chose {comp_choice}")
        else:
            print(f"Well done. The computer chose {comp_choice} and failed")
            user_rating += 100
