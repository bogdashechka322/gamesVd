import random

def prime_game():
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    
    correct_answers = 0
    questions_count = 3
    
    for _ in range(questions_count):
        number = random.randint(1, 100)
        is_number_prime = is_prime(number)
        correct_answer = "yes" if is_number_prime else "no"
        
        print(f"Question: {number}")
        user_answer = input("Your answer: ").lower().strip()
        
       
        normalized_answer = user_answer
        
        if normalized_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    if correct_answers == questions_count:
        print(f"Congratulations, {name}!")


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


if __name__ == "__main__":
    prime_game()
