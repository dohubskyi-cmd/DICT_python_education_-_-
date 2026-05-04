import random

def initialize_game():
    full_set = [[i, j] for i in range(7) for j in range(i, 7)]
    while True:
        random.shuffle(full_set)
        stock, computer, player = full_set[:14], full_set[14:21], full_set[21:]
        for i in range(6, -1, -1):
            if [i, i] in computer:
                s, status = [[i, i]], "player"
                computer.remove([i, i])
                return stock, computer, player, s, status
            if [i, i] in player:
                s, status = [[i, i]], "computer"
                player.remove([i, i])
                return stock, computer, player, s, status

def display_and_check(stock, computer, player, snake, status):
    print("=" * 70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(computer)}\n")
    
    if len(snake) > 6:
        print(f"{snake[0]}{snake[1]}{snake[2]}...{snake[-3]}{snake[-2]}{snake[-1]}\n")
    else:
        print(f"{''.join(str(p) for p in snake)}\n")
        
    print("Your pieces:")
    for i, piece in enumerate(player, 1):
        print(f"{i}:{piece}")
    
    if not player: return "The game is over. You won!"
    if not computer: return "The game is over. The computer won!"
    if snake[0][0] == snake[-1][1] and sum(p.count(snake[0][0]) for p in snake) == 8:
        return "The game is over. It's a draw!"
    
    if status == "computer":
        print("\nStatus: Computer is about to make a move. Press Enter to continue...")
    else:
        print("\nStatus: It's your turn to make a move. Enter your command.")
    return None

def main():
    stock, computer, player, snake, status = initialize_game()
    
    while True:
        end_msg = display_and_check(stock, computer, player, snake, status)
        if end_msg:
            print(f"Status: {end_msg}")
            break
            
        if status == "player":
            while True:
                try:
                    move = int(input("> "))
                    if abs(move) > len(player): raise ValueError
                    
                    if move == 0:
                        if stock: player.append(stock.pop())
                        break
                    
                    idx = abs(move) - 1
                    p = player[idx]
                    target = snake[-1][1] if move > 0 else snake[0][0]
                    if target in p:
                        if move > 0:
                            if p[0] != target: p.reverse()
                            snake.append(player.pop(idx))
                        else:
                            if p[1] != target: p.reverse()
                            snake.insert(0, player.pop(idx))
                        break
                    else:
                        print("Illegal move. Please try again.")
                except ValueError:
                    print("Invalid input. Please try again.")
            status = "computer"
        else:
            input("> ")
            scores = {i: 0 for i in range(7)}
            for p in computer + snake:
                scores[p[0]] += 1; scores[p[1]] += 1
            
            comp_list = sorted(computer, key=lambda x: scores[x[0]] + scores[x[1]], reverse=True)
            moved = False
            for p in comp_list:
                if snake[-1][1] in p:
                    if p[0] != snake[-1][1]: p.reverse()
                    snake.append(p); computer.remove(p); moved = True; break
                elif snake[0][0] in p:
                    if p[1] != snake[0][0]: p.reverse()
                    snake.insert(0, p); computer.remove(p); moved = True; break
            
            if not moved and stock:
                computer.append(stock.pop())
            status = "player"

if __name__ == "__main__":
    main()
