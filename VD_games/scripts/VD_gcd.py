import random

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd_game():
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    correct_answers_needed = 3
    correct_answers = 0

    while correct_answers < correct_answers_needed:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        correct_answer = calculate_gcd(num1, num2)

        print(f"Question: {num1} {num2}")
        user_answer = input("Your answer: ")

        try:
            if int(user_answer) == correct_answer:
                print("Correct!")
                correct_answers += 1
            else:
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
                print(f"Let's try again, {name}!")
                return
        except ValueError:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    gcd_game()
