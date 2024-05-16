import random

def users_name():
    """
    Enter the user's name and validate the input with exception handling
    """
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
    return user_name
user = users_name()



def play_game():

    options = ('rock', 'paper', 'scissors') # Tuple used as these are not being changes, uses less memory than list
    user_choice = None
    user_score = 0
    computer_score = 0

    for i in range(4):
       # while user_choice not in options: # Loops until the user enters correct value
        print("Round ", i+1)
        user_choice = input("What's your choice? (rock, paper, scissors): ")
        computer_choice = random.choice(options)
        print(f"{user}'s choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        if user_choice == computer_choice:
            print('tie')
            #i += 1
        elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
            user_score += 1
            #i += 1
            print('user wins')
        else:
            computer_score +=1
            print('computer wins')
            #i += 1
    return user_score, computer_score

def display_score():
    print(f"{user} = {user_score}\n Computer = {computer_score}")
    if user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("Computer wins!")
    else:
        print("It's a tie!")

user_score, computer_score = play_game()
display_score()