logo="""
 ______     _________  ____    _____  _    _____   _     _     _     ____  _________   
/  __/ \ /\/  __/ ___\/ ___\  /__ __\/ \ //  __/  / \  // \ /\/ \__//  _ \/  __/  __\  
| |  | | |||  \ |    \|    \    / \  | |_||  \    | |\ || | ||| |\/|| | //|  \ |  \/|  
| |_// \_/||  /_\___ |\___ |    | |  | | ||  /_   | | \|| \_/|| |  || |_\\|  /_|    /  
\____\____/\____\____/\____/    \_/  \_/ \\____\  \_/  \\____/\_/  \\____/\____\_/\_\  
                                                                                       
"""
import random

easy_level = 10
hard_level = 5

def check_answer(user_choice, computer_choice, turns):
    
    if user_choice > computer_choice:
        print("Too high.")
        return turns - 1
    elif user_choice < computer_choice:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {computer_choice}")
        return 0  

def set_difficulty():
    
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return easy_level
    else:
        return hard_level

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = random.randint(1, 100)  
    print(f"Pssst, the correct answer is {answer}")  

    turns = set_difficulty()  

    guess = 0  
    while guess != answer and turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0 and guess != answer:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
