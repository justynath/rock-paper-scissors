import random

options = ('rock', 'paper', 'scissors') #tuple used as these are not being changes, uses less memory than list
users_choice = None
computers_choice = random.choice(options)

users_choice = input("What's your choice? (rock, paper, scissor): ")

print(f"User's choice: {users_choice}")
print(f"Computer's choice: {computers_choice}")