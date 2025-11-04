import random
import string

def play_game(word):
    lives = 8
    guessed_letters = set()
    display_word = ["-"] * len(word)
    
    print("-" * len(word)) 

    while lives > 0 and "-" in display_word:
        
        print(f"Input a letter: ", end="")
        guess = input()
        
        if len(guess) != 1:
            print("You should input a single letter")
            print("".join(display_word))
            continue
            
        if guess not in string.ascii_lowercase:
            print("Please enter a lowercase English letter")
            print("".join(display_word))
            continue
            
        if guess in guessed_letters:
            print("You've already guessed this letter")
            print("".join(display_word))
            continue
            
        guessed_letters.add(guess)

        if guess in word:
            for i, char in enumerate(word):
                if char == guess:
                    display_word[i] = guess
            print("".join(display_word))
        else:
            print("That letter doesn't appear in the word")
            lives -= 1
            print("".join(display_word))
        
        if "-" not in display_word:
            print(f"You guessed the word {word}!")
            print("You survived!")
            return

    if "-" in display_word:
        print("You lost!")
        return

def main():
    WORD_LIST = ['python', 'java', 'javascript', 'php']
    print("HANGMAN")
    
    while True:
        print('Type "play" to play the game, "exit" to quit: ', end="")
        choice = input().lower()
        
        if choice == "play":
            SECRET_WORD = random.choice(WORD_LIST)
            play_game(SECRET_WORD)
        elif choice == "exit":
            break
        else:
            pass

if __name__ == "__main__":
    main()
