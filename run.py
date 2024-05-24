import random
import gspread
import colorama
from google.oauth2.service_account import Credentials
from colorama import Fore

colorama.init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('scores_record')

scores = SHEET.worksheet('scores')

all_data = scores.get_all_values()
scores_worksheet = SHEET.worksheet('scores')


def enter_user_name():
    """
    Enter the user's name and validate the input with exception handling
    """
    print(f"{Fore.CYAN}R O C K\nP A P E R\nS C I S S O R S\n")

    while True:
        try:
            user_name = str(input(f"{Fore.WHITE}Enter your name:\n{Fore.YELLOW}"))
            if len(user_name) > 2:
                print(f"\n{Fore.WHITE}Welcome to the game {Fore.YELLOW}{user_name}\n")
                break
            else:
                raise TypeError
        except TypeError:
            print(f"{Fore.RED}Name must be at least three characters")
            continue
    return user_name


user = enter_user_name()


def how_many_rounds():
    """
    Function to select how many rounds a user wants to play in one game
    """
    while True:
        try:
            number_of_rounds = int(input(f"\n{Fore.WHITE}How many times you want to play (max 8)?:\n{Fore.YELLOW}"))
            if 1 <= number_of_rounds <= 8:
                print(f"{Fore.WHITE}You selected {Fore.YELLOW}{number_of_rounds} {Fore.WHITE}rounds")
                break
            else:
                raise ValueError
        except ValueError:
            print(f"{Fore.RED}Please enter a number between 1 and 8")
    return number_of_rounds


def play_game():
    """
    Function to define the game (set number of rounds):
    - player and computer chosing the option
    - chioces are compared
    - score incremented for the winner of the round
    """
    options = ('rock', 'paper', 'scissors')
    user_choice = None
    user_score = 0
    computer_score = 0

    rounds = how_many_rounds()

    for i in range(rounds):
        # Validate input. Only allow values in options tuple
        while True:
            increment = i+1
            print(f"\n{Fore.CYAN}Round {increment}")
            # Allow correct values with capital letters and spaces
            user_choice = input(f"{Fore.WHITE}What's your choice? (rock, paper, scissors):\n{Fore.YELLOW}").lower().strip()
            computer_choice = random.choice(options)
            if user_choice not in options:
                print(f"{Fore.RED}{user_choice} is not an option")
                continue
            else:
                break

        print(f"{Fore.YELLOW}{user}{Fore.WHITE}'s choice: {Fore.YELLOW}{user_choice}")
        print(f"{Fore.WHITE}Computer's choice: {Fore.GREEN}{computer_choice}")

        if (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
            user_score += 1
        elif (user_choice == 'rock' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'rock'):
            computer_score += 1
    return user_score, computer_score


def show_instructions():
    """
    Function gives two option: 1. Read the instruction 2. Play the game
    If option 1, two further options: play or quit
    If option 2, game starts
    """
    user_score = 0
    computer_score = 0
    print(f"{Fore.WHITE}1. Instructions \n2. Play the game \n")
    # Validate input, only allow 1 or 2
    while True:
        try:
            instr_choice = int(input(f"Enter '1' to read the instructions. Enter '2' to start the game:\n{Fore.YELLOW}"))
            if instr_choice == 1:
                # Get text from the file and display
                f = open('instructions.txt')
                lines = f.read()
                f.close()
                print(f"{Fore.CYAN}{lines}")
                while True:
                    try:
                        # Reconfirm with the user if they want to proceed
                        start_game = input(f"{Fore.WHITE}Would you like to play (y/n)?:\n{Fore.YELLOW}").lower()
                        if start_game == 'y':
                            return
                        elif start_game == 'n':
                            print(f"{Fore.CYAN}Bye, {Fore.YELLOW}{user}")
                            quit()
                        else:
                            raise ValueError
                    except ValueError:
                        print(f"{Fore.RED}Please select 'y' or 'n' only")
            elif instr_choice == 2:
                return
            else:
                raise ValueError
        except ValueError:
            print(f"{Fore.RED}Please select '1' or '2' only")


def display_score():
    """
    Final score is displayed and the winner announced
    """
    points = 0  # This variable will be used for updating the scores record in google sheet
    print(f"\n{Fore.YELLOW}{user} {Fore.WHITE}= {Fore.YELLOW}{user_score} {Fore.WHITE}\nComputer = {Fore.GREEN}{computer_score}")
    if user_score > computer_score:
        print(f"\n{Fore.YELLOW}{user} WINS!\n")
        points = 2
    elif user_score < computer_score:
        print(f"\n{Fore.GREEN}COMPUTER WINS!\n")
        points = 0
    else:
        print(f"\n{Fore.WHITE}IT'S A TIE!\n")
        points = 1
    return points


show_instructions()
user_score, computer_score = play_game()


def calculate_new_score_row():
    """
    Function to calculate the new overall score
    """
    new_name_row = []
    found = False
    for row in all_data:
        # Check if the name already exists and find the row
        if user in row:
            name_row = row
            # print('Found:', name_row) #testing
            found = True
            # Calculate new values for the worksheet: add one to games played, add 'points' to poits column, calculate new success rate
            games_played = int(name_row[1])
            games_played += 1
            points_total = int(name_row[2])
            new_points_total = points_total + points
            success_rate = round((new_points_total/(games_played*2))*100)
            new_name_row = [user, games_played, new_points_total, success_rate]
            # print(new_name_row) #testing
            break
    if not found:
        success_rate = round((points/2)*100)
        new_name_row = [user, 1, points, success_rate]
    return new_name_row


def update_scores_record(data):
    """
    Function to update the scores record in google sheet:
    - add one to numebr of games played
    - add two to points if the game is won
    - add one to points if it is a tie
    - future: calculate the success rate as percentage
    """
    while True:
        try:
            print(f"{Fore.RED}IN ORDER TO GET THE ACCURATE SUCCESS RATE IT IS RECOMMENDED TO ALWAYS UPDATE YOUR SCORE\n")
            add_score = input(f"{Fore.WHITE}Would you like to proceed with updating your overall score record (y/n)?\n{Fore.YELLOW}").lower()
            if add_score == 'y':
                print(f"\n{Fore.WHITE}Updating scores record...\n")
                found = False
                for row in all_data:
                    if user in row:
                        found = True
                        # Find the cell where the existing name is and convert the answer to a string
                        cell = scores_worksheet.find(user)
                        cell_string = str(cell)
                        # Remove the part up to the row number
                        split_cell = str(cell_string.split('<Cell R')[1])
                        # Remove the part from 'c' until the end.
                        # This two step method allows returning an integer with any number of digits
                        find_row_num = int(split_cell.rsplit('C')[0])
                        # print(find_row_num) #testing
                        # Delete the existing row and add new row with he new data
                        scores_worksheet.delete_rows(find_row_num)
                        scores_worksheet.append_row(data)
                if not found:
                    scores_worksheet.append_row(data)
                print(f"{Fore.WHITE}Scores worksheet updated successfully.\n")
                break
            elif add_score == 'n':
                return
            else:
                raise ValueError
        except ValueError:
            print(f"{Fore.RED}Please select 'y' or 'n' only")


def display_overall_score():
    """
    Function to display current overall score from the google sheet
    """
    # Get the headings from the scores worksheet's first row
    headings = SHEET.worksheet("scores").row_values(1)
    # Finding the row number where the values are 
    cell = scores_worksheet.find(user)
    cell_string = str(cell)
    split_cell = str(cell_string.split('<Cell R')[1])
    find_row_num = int(split_cell.rsplit('C')[0])
    row_with_score = SHEET.worksheet("scores").row_values(find_row_num)
    i = 1
    # Printing the overall score
    print(f"{Fore.YELLOW}{user}{Fore.WHITE}'s overall score is:\n{Fore.YELLOW}---------------------------")
    while i < 3:
        print(f"{headings[i]}: {Fore.YELLOW}{row_with_score[i]}")
        i += 1
    print(f"{Fore.WHITE}Success Rate: {Fore.YELLOW}{row_with_score[3]}%{Fore.YELLOW}\n---------------------------")


points = display_score()
new_overall_score = calculate_new_score_row()
updated_score = update_scores_record(new_overall_score)
display_overall_score()



print(f"""\n{Fore.WHITE}Thank you for playing, {Fore.YELLOW}{user}
{Fore.WHITE}Click {Fore.RED}'Start Game' {Fore.WHITE}on the top of this page to play again""")
