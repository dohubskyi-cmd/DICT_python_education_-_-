import random

friends = {}

try:
    num_friends = int(input("Enter the number of friends joining (including you):\n> "))
except ValueError:
    num_friends = 0

if num_friends <= 0:
    print("\nNo one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    for _ in range(num_friends):
        name = input("> ")
        friends[name] = 0
    
    try:
        total_amount = float(input("\nEnter the total amount:\n> "))
    except ValueError:
        total_amount = 0.0

    split_amount = round(total_amount / num_friends, 2)
    for name in friends:
        friends[name] = split_amount

    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    choice = input("> ")

    if choice.lower() == 'yes':
        lucky_one = random.choice(list(friends.keys()))
        print(f"\n{lucky_one} is the lucky one!")

        new_split_amount = 0.0
        if num_friends > 1:
            new_split_amount = round(total_amount / (num_friends - 1), 2)
        
        for name in friends:
            if name == lucky_one:
                friends[name] = 0
            else:
                friends[name] = new_split_amount
        
        print(friends)

    else:
        print("\nNo one is going to be lucky")
        print(friends)
