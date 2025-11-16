import random

def progression_game():
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")
    
    correct_answers_needed = 3
    correct_answers = 0
    
    while correct_answers < correct_answers_needed:
        progression_str, correct_answer = generate_arithmetic_progression()
        
        print(f"Question: {progression_str}")
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

def generate_arithmetic_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    progression = []
    for index in range(length):
        current_element = start + index * step
        progression.append(current_element)
    hidden_position = random.randint(0, length - 1)
    correct_answer = progression[hidden_position]
    progression_display = []
    for index in range(length):
        if index == hidden_position:
            progression_display.append("..")
        else:
            progression_display.append(str(progression[index]))
    return " ".join(progression_display), correct_answer



if __name__ == "__main__":
    progression_game()
