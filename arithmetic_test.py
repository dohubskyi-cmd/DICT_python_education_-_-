import random

class ArithmeticTest:
    def __init__(self):
        self.correct_answers = 0

    def get_valid_int(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Incorrect format. Please enter a number.")

    def run_test(self):
        print("Starting Arithmetic Test! Answer 5 questions.")
        for i in range(1, 6):
            a, b = random.randint(2, 9), random.randint(2, 9)
            print(f"Question {i}: {a} * {b} = ?")
            
            user_answer = self.get_valid_int("Your answer: ")
            
            if user_answer == a * b:
                print("Right!")
                self.correct_answers += 1
            else:
                print("Wrong!")
        
        print(f"Test finished. Your score: {self.correct_answers}/5")

if __name__ == "__main__":
    test = ArithmeticTest()
    test.run_test()
