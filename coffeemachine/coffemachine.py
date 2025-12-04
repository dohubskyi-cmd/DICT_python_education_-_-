class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "choosing_action"

    def process_input(self, user_input):
        if self.state == "choosing_action":
            self.action(user_input)
        elif self.state == "choosing_coffee":
            self.buy_coffee(user_input)
        elif self.state == "filling_water":
            self.fill_water(user_input)
        elif self.state == "filling_milk":
            self.fill_milk(user_input)
        elif self.state == "filling_beans":
            self.fill_beans(user_input)
        elif self.state == "filling_cups":
            self.fill_cups(user_input)

    def action(self, user_input):
        if user_input == "buy":
            print()
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            self.state = "choosing_coffee"
        elif user_input == "fill":
            print()
            print("Write how many ml of water you want to add:")
            self.state = "filling_water"
        elif user_input == "take":
            print()
            print(f"I gave you {self.money}")
            print()
            self.money = 0
        elif user_input == "remaining":
            print()
            self.show_status()
            print()
        elif user_input == "exit":
            exit()

    def buy_coffee(self, user_input):
        if user_input == "back":
            self.state = "choosing_action"
            print()
            return

        water_needed = 0
        milk_needed = 0
        beans_needed = 0
        cost = 0

        if user_input == "1":
            water_needed = 250
            beans_needed = 16
            cost = 4
        elif user_input == "2":
            water_needed = 350
            milk_needed = 75
            beans_needed = 20
            cost = 7
        elif user_input == "3":
            water_needed = 200
            milk_needed = 100
            beans_needed = 12
            cost = 6

        if self.water < water_needed:
            print("Sorry, not enough water!")
        elif self.milk < milk_needed:
            print("Sorry, not enough milk!")
        elif self.beans < beans_needed:
            print("Sorry, not enough coffee beans!")
        elif self.cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= water_needed
            self.milk -= milk_needed
            self.beans -= beans_needed
            self.cups -= 1
            self.money += cost

        print()
        self.state = "choosing_action"

    def fill_water(self, user_input):
        self.water += int(user_input)
        print("Write how many ml of milk you want to add:")
        self.state = "filling_milk"

    def fill_milk(self, user_input):
        self.milk += int(user_input)
        print("Write how many grams of coffee beans you want to add:")
        self.state = "filling_beans"

    def fill_beans(self, user_input):
        self.beans += int(user_input)
        print("Write how many disposable coffee cups you want to add:")
        self.state = "filling_cups"

    def fill_cups(self, user_input):
        self.cups += int(user_input)
        print()
        self.state = "choosing_action"

    def show_status(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")


machine = CoffeeMachine()

while True:
    if machine.state == "choosing_action":
        print("Write action (buy, fill, take, remaining, exit):")
    
    user_input = input()
    machine.process_input(user_input)
