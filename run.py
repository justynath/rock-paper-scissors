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

def play():

    options = ('rock', 'paper', 'scissors') # Tuple used as these are not being changes, uses less memory than list
    user_choice = None
    computer_choice = random.choice(options)
    user_score = 0
    computer_score = 0

    while user_choice not in options: # Loops until the user enters correct value
        user_choice = input("What's your choice? (rock, paper, scissors): ")

    print(f"{user}'s choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")


# this section neets fixing
    if user_choice == computer_choice:
        print('tie')
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        user_score += 1
        print('user wins')
    else:
        computer_score +=1
        print('computer wins')
    return user_score, computer_score
user_score, computer_score = play()

# up to this section (adding on scores)

def display_score():
    print(f"{user} = {user_score}\n Computer = {computer_score}")
    if user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("Computer wins!")
    else:
        print("It's a tie!")


def play_game():
    i = 0
    while i < 3:
       play()
       i +=1
    display_score()

play_game()