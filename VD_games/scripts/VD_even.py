import random


def welcome_user():
    print("Welcome to the VD-games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def is_even(number):
    return number % 2 == 0


def play_even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    correct_answers = 0
    rounds_to_win = 3
    
    while correct_answers < rounds_to_win:
        number = random.randint(1, 100)
        correct_answer = "yes" if is_even(number) else "no"
        
        print(f"Question: {number}")
        user_answer = input("Your answer: ").strip().lower()
        
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")


def main():
    play_even_game()


if __name__ == "__main__":
    main()
