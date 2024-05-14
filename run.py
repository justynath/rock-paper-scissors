import random

def play_game():

    options = ('rock', 'paper', 'scissors') # tuple used as these are not being changes, uses less memory than list
    users_choice = None
    computers_choice = random.choice(options)

    while users_choice not in options:
        users_choice = input("What's your choice? (rock, paper, scissor): ")

    print(f"User's choice: {users_choice}")
    print(f"Computer's choice: {computers_choice}")

    if users_choice == computers_choice:
        print('tie')
    elif (users_choice == 'rock' and computers_choice == 'scissors') or (users_choice == 'paper' and computers_choice == 'rock') or (users_choice == 'scissors' and computers_choice == 'paper'):
        print('user wins')
    else:
        print('computer wins')

play_game()