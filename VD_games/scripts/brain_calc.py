import random
def generate_question():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    operation = random.choice(['+', '-', '*'])
    if operation == '+':
        answer = a + b
    elif operation == '-':
        answer = a - b
    else:  # '*'
        answer = a * b
    question = f"{a} {operation} {b}"
    return question, answer

def run_game(game_name, game_description, question_generator, rounds=3):
    print("Welcome to the VD games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_description)
    for i in range(rounds):
        question, correct_answer = question_generator()
        print(f"Question: {question}")
        while True:
            try:
                user_answer = int(input("Your answer: "))
                break
            except ValueError:
                print("Please enter a valid number!")
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")

def play_calc():
    run_game(
        game_name="calc",
        game_description="What is the result of the expression?",
        question_generator=generate_question,
        rounds=3
    )

if __name__ == "__main__":
    play_calc()
    
