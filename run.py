import random
import sys

def users_name():
    """
    Enter the user's name and validate the input with exception handling
    """
    while True: # Never ending loop
        try:
            user_name = str(input("Enter your name: "))
            if len(user_name) > 2:
                print(f"Welcome to the game {user_name}\n")
                break
            else:
                raise TypeError
        except TypeError:
            print("Name must be at least three characters")
            continue
    return user_name

user = users_name()

def play_game():

    options = ('rock', 'paper', 'scissors') # Tuple used as these are not being changes, uses less memory than list
    user_choice = None
    user_score = 0
    computer_score = 0

    for i in range(4):
        # Validate input. Only allow values in options tupe
        while True:
            print("Round ", i+1)
            # Allow correct values with capital letters and spaces
            user_choice = input("What's your choice? (rock, paper, scissors): ").lower().strip()
            computer_choice = random.choice(options)
            if user_choice not in options:
                print(f"{user_choice} is not an option")
                continue
            else:
                break
        print(f"{user}'s choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        if (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
            user_score += 1
            #print('user wins')
        elif (user_choice == 'rock' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'rock'):
            computer_score +=1
            #print('computer wins')
    return user_score, computer_score

def show_instructions():
    user_score = 0
    computer_score = 0
    print("1. Instructions \n2. Play the game \n")
    instr_choice = int(input("Enter '1' to read the instructions. Enter '2' to start the game: "))
    if instr_choice == 1:
        f = open('instructions.txt')
        lines = f.read()
        f.close()
        print(lines)
        start_game = input("Would you like to play (y/n)?: ").lower()
        if start_game == 'y':
            return #play_game()
        elif start_game == 'n':
            sys.exit() #print("test")
    #elif instr_choice == 2:
        #play_game()

show_instructions()
user_score, computer_score = play_game()

def display_score():
    print(f"{user} = {user_score} Computer = {computer_score}")
    if user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("Computer wins!")
    else:
        print("It's a tie!")

display_score()