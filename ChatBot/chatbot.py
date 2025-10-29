print("Hello! My name is Dmutro_Bot.")
print("I was created in 2025.")
print("Please, remind me your name.")
user_name = input()
print(f"What a great name you have,{user_name}!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {age}; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
count_to = int(input())
for i in range(count_to + 1):
    print(f"{i} !")
print("Completed, have a nice day!")
correct_answer = '3'
while True:
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To determine the execution time of a program.")
    print("3. To decompose a program into several small subroutines.")
    print("4. To interrupt the execution of a program.")
    answer = input()
    if answer == correct_answer:
        break
    else:
        print("Please, try again.")

print("Completed, have a nice day!")
print("Congratulations, have a nice day!")
