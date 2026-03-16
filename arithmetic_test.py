import random

class ArithmeticTest:
    def __init__(self):
        self.correct_answers = 0
        self.total_questions = 5
        self.results_file = "test_results.txt"

    def get_valid_int(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Incorrect format. Please enter a number.")

    def run_test(self):
        print("--- Arithmetic Test: Levels 1 & 2 ---")
        
        for i in range(1, self.total_questions + 1):
            level = random.randint(1, 2)
            
            if level == 1:
                num1, num2 = random.randint(2, 9), random.randint(2, 9)
                expected = num1 * num2
                print(f"Question {i} (Level 1): {num1} * {num2} = ?")
            else:
                num = random.randint(11, 20)
                expected = num ** 2
                print(f"Question {i} (Level 2): {num}^2 = ?")
            
            user_answer = self.get_valid_int("Your answer: ")
            
            if user_answer == expected:
                print("Right!")
                self.correct_answers += 1
            else:
                print(f"Wrong! The correct answer was {expected}")
        
        self.save_results()

    def save_results(self):
        score_text = f"Test finished. Your score: {self.correct_answers}/{self.total_questions}"
        print(score_text)
        
        try:
            with open(self.results_file, "a", encoding="utf-8") as f:
                f.write(f"Result: {self.correct_answers}/{self.total_questions}\n")
            print(f"Results saved to {self.results_file}")
        except IOError:
            print("Error: Could not save results to file.")

if __name__ == "__main__":
    test = ArithmeticTest()
    test.run_test()
