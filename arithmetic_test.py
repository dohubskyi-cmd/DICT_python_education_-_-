import random

class ArithmeticTest:
    def __init__(self):
        self.correct_answers = 0
        self.total_questions = 5
        self.level = 0
        self.level_description = ""

    def get_valid_int(self, prompt):
        """Перевірка на коректність введення цілого числа."""
        while True:
            user_input = input(prompt).strip()
            try:
                return int(user_input)
            except ValueError:
                print("Incorrect format.")

    def select_level(self):
        """Етап 3: Вибір рівня складності."""
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        
        while True:
            choice = input("> ").strip()
            if choice == "1":
                self.level = 1
                self.level_description = "simple operations with numbers 2-9"
                break
            elif choice == "2":
                self.level = 2
                self.level_description = "integral squares of 11-29"
                break
            else:
                print("Incorrect format.")
                print("Which level do you want? Enter a number:")
                print("1 - simple operations with numbers 2-9")
                print("2 - integral squares of 11-29")

    def run_test(self):
        """Основний цикл тестування на 5 питань."""
        self.select_level()

        for i in range(1, self.total_questions + 1):
            if self.level == 1:
                num1, num2 = random.randint(2, 9), random.randint(2, 9)
                operation = random.choice(['+', '-', '*'])
                
                if operation == '+':
                    expected = num1 + num2
                elif operation == '-':
                    expected = num1 - num2
                else:
                    expected = num1 * num2
                
                print(f"{num1} {operation} {num2}")
            
            else:
                num = random.randint(11, 29)
                expected = num ** 2
                print(f"{num}")

            user_answer = self.get_valid_int("> ")
            
            if user_answer == expected:
                print("Right!")
                self.correct_answers += 1
            else:
                print("Wrong!")

        self.finish_and_save()

    def finish_and_save(self):
        """Виведення результату та запис у файл (Етап 3)."""
        score_text = f"Your mark is {self.correct_answers}/{self.total_questions}."
        print(f"{score_text} Would you like to save the result? Enter yes or no.")
        
        save_choice = input("> ").strip().lower()
        
        if save_choice in ["yes", "y"]:
            name = input("What is your name?\n> ").strip()
            
            result_line = f"{name}: {self.correct_answers}/{self.total_questions} in level {self.level} ({self.level_description}).\n"
            
            try:
                with open("results.txt", "a", encoding="utf-8") as f:
                    f.write(result_line)
                print('The results are saved in "results.txt".')
            except IOError:
                print("Error: Could not save results to file.")
        else:
            pass

if __name__ == "__main__":
    test = ArithmeticTest()
    test.run_test()
