import random

def users_name():
    while True: # Never ending loop
        try:
            user_name = str(input("Enter your name: "))
            if len(user_name) > 2:
                print(f"Welcome to the game {user_name}")
                break
            else:
                raise TypeError
        except TypeError:
            print("Name must be at least three characters")
            continue

users_name()

def play_game():

    options = ('rock', 'paper', 'scissors') # tuple used as these are not being changes, uses less memory than list
    user_choice = None
    computer_choice = random.choice(options)

    while user_choice not in options:
        user_choice = input("What's your choice? (rock, paper, scissor): ")

    print(f"User's choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    if user_choice == computer_choice:
        print('tie')
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        print('user wins')
    else:
        print('computer wins')

play_game()