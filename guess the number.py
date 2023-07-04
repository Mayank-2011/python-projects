logo = '''
 ████████    ████████████████████    █████████   ████████    ███    ███    ████    ████████████████████  
██     ██    ███    ██    ██            ██  ██   ███         ████   ███    █████  █████   ███    ██   ██ 
██   ████    ██████ █████████████       ██  ███████████      ██ ██  ███    ███ ████ ████████████ ██████  
██    ███    ███         ██    ██       ██  ██   ███         ██  ██ ███    ███  ██  ███   ███    ██   ██ 
 ██████ █████████████████████████       ██  ██   ████████    ██   ████████████      ███████████████   ██ 
                                                                                                         
                                                                                                         
'''

import random 
def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game")
    
    print("I'm guessing a number between 1 and 100.")
    chosen_number = random.randint(1,100)


    choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = 0
    if choice == 'hard':
        attempts = 5
    elif choice == 'easy':
        attempts = 10
    
    is_game_over = False
    
    while not is_game_over:
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            is_game_over = True
        else:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
        
            if guess == chosen_number:
                print(f"You got it! The answer was {guess}.")
                is_game_over = True
            elif guess > chosen_number:
                print("Too high")
                attempts -=1
            elif guess < chosen_number:
                print("Too Low")
                attempts -=1
        

play_game()
