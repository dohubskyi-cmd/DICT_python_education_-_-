import random

print("How many pencils would you like to use:")
while True:
    line = input()
    if not line.isdigit():
        print("The number of pencils should be numeric")
        continue
    
    pencils = int(line)
    if pencils == 0:
        print("The number of pencils should be positive")
        continue
    break

print("Who will be the first (John, Jack):")
while True:
    name = input()
    if name == "John" or name == "Jack":
        break
    else:
        print("Choose between 'John' and 'Jack'")

player1 = "John"
player2 = "Jack"

while pencils > 0:
    print("|" * pencils)
    print(f"{name}'s turn:")
    
    if name == player2:
        if pencils % 4 == 0:
            move = 3
        elif pencils % 4 == 3:
            move = 2
        elif pencils % 4 == 2:
            move = 1
        else:
            move = random.randint(1, 3)
        
        if move > pencils:
            move = pencils
            
        print(move)
    else:
        while True:
            line = input()
            if line not in ['1', '2', '3']:
                print("Possible values: '1', '2' or '3'")
                continue
            
            move = int(line)
            if move > pencils:
                print("Too many pencils were taken")
                continue
            break

    pencils -= move
    
    if pencils == 0:
        winner = player2 if name == player1 else player1
        print(f"{winner} won!")
        break
    
    name = player2 if name == player1 else player1
