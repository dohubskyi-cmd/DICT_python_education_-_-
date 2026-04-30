import random
import sqlite3

def luhn_check(num):
    digits = [int(d) for d in num]
    check_digit = digits.pop()
    for i in range(len(digits)):
        if (i + 1) % 2 != 0:
            digits[i] = digits[i] * 2 - 9 if digits[i] * 2 > 9 else digits[i] * 2
    return (sum(digits) + check_digit) % 10 == 0

def execute_transaction(card, action):
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    if action == "balance":
        cur.execute("SELECT balance FROM card WHERE number = ?", (card,))
        return cur.fetchone()[0]
    elif action == "income":
        amount = int(input("\nEnter income:\n> "))
        cur.execute("UPDATE card SET balance = balance + ? WHERE number = ?", (amount, card))
        print("Income was added!")
    elif action == "close":
        cur.execute("DELETE FROM card WHERE number = ?", (card,))
        print("\nThe account has been closed!")
    conn.commit()
    conn.close()

def do_transfer(sender):
    target = input("\nTransfer\nEnter card number:\n> ")
    if target == sender:
        return print("You can't transfer money to the same account!")
    if not luhn_check(target):
        return print("Probably you made a mistake in the card number. Please try again!")
    
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    cur.execute("SELECT balance FROM card WHERE number = ?", (target,))
    if not cur.fetchone():
        return print("Such a card does not exist.")
    
    amount = int(input("Enter how much money you want to transfer:\n> "))
    cur.execute("SELECT balance FROM card WHERE number = ?", (sender,))
    if amount > cur.fetchone()[0]:
        return print("Not enough money!")
    
    cur.execute("UPDATE card SET balance = balance - ? WHERE number = ?", (amount, sender))
    cur.execute("UPDATE card SET balance = balance + ? WHERE number = ?", (amount, target))
    conn.commit()
    conn.close()
    print("Success!")

def main():
    conn = sqlite3.connect('card.s3db')
    conn.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)')
    conn.close()
    while True:
        choice = input("\n1. Create account\n2. Log in\n0. Exit\n> ")
        if choice == "1":
            iin, acc = "400000", "".join([str(random.randint(0, 9)) for _ in range(9)])
            ds = [int(d) for d in iin + acc]
            for i in range(len(ds)):
                if (i + 1) % 2 != 0: ds[i] = ds[i]*2-9 if ds[i]*2>9 else ds[i]*2
            c_num = iin + acc + str((10-(sum(ds)%10))%10)
            pin = "".join([str(random.randint(0, 9)) for _ in range(4)])
            conn = sqlite3.connect('card.s3db'); conn.execute("INSERT INTO card (number, pin) VALUES (?,?)", (c_num, pin)); conn.commit(); conn.close()
            print(f"\nYour card has been created\nYour card number:\n{c_num}\nYour card PIN:\n{pin}")
        elif choice == "2":
            cn, pn = input("\nEnter card number:\n> "), input("Enter PIN:\n> ")
            conn = sqlite3.connect('card.s3db'); cur = conn.cursor(); cur.execute("SELECT * FROM card WHERE number=? AND pin=?", (cn, pn)); user = cur.fetchone(); conn.close()
            if user:
                print("\nYou have successfully logged in!")
                while True:
                    act = input("\n1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n> ")
                    if act == "1": print(f"\nBalance: {execute_transaction(cn, 'balance')}")
                    elif act == "2": execute_transaction(cn, "income")
                    elif act == "3": do_transfer(cn)
                    elif act == "4": execute_transaction(cn, "close"); break
                    elif act == "5": print("\nYou have successfully logged out!"); break
                    elif act == "0": exit(print("\nBye!"))
            else: print("\nWrong card number or PIN!")
        elif choice == "0": exit(print("\nBye!"))

if __name__ == "__main__":
    main()
