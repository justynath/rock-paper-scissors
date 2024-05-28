import random
import gspread
import colorama
from google.oauth2.service_account import Credentials
from colorama import Fore

colorama.init(autoreset=True)


# Try to connect to Googlesheets, if error notify user
try:
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
        ]
except FileNotFoundError:
    print("Error: please refresh the browser\n")

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('scores_record')


def enter_user_name():
    """
    Enter the user's name and validate the input with exception handling
    """
    print(f"""{Fore.CYAN}
    R O C K
    P A P E R
    S C I S S O R S\n""")

    while True:
        try:
            user_name = str(input(f"""
    {Fore.WHITE}Enter your name: {Fore.YELLOW}"""))
            if user_name.isdigit():
                raise TypeError
            elif len(user_name) > 2:
                print(f"""{Fore.WHITE}
        Welcome to the game {Fore.GREEN}{user_name}\n""")
                break
            else:
                raise ValueError
        except ValueError:
            print(f"""{Fore.CYAN}
    Name must be at least three characters""")
        except TypeError:
            print(f"""{Fore.CYAN}
    Invalid value""")
            continue
    return user_name


def show_instructions():
    """
    Function gives two option: 1. Read the instruction 2. Play the game
    If option 1, two further options: play or quit
    If option 2, game starts
    """
    print(f"""{Fore.WHITE}
    1. Instructions
    2. Play the game""")
    # Validate input, only allow 1 or 2
    while True:
        try:
            instr_choice = int(input(f"""
    Enter '1' to read the instructions.\
Enter '2' to start the game: {Fore.YELLOW}"""))
            if instr_choice == 1:
                # Get text from the file and display
                f = open('instructions.txt')
                lines = f.read()
                f.close()
                print(f"""
    {Fore.CYAN}{lines}""")
                while True:
                    try:
                        # Reconfirm with the user if they want to proceed
                        start_game = input(f"""
    {Fore.WHITE}Would you like to play (y/n)?: {Fore.YELLOW}""").lower()
                        if start_game == 'y':
                            return
                        elif start_game == 'n':
                            print(f"""
    {Fore.WHITE}Bye, {Fore.YELLOW}{user}""")
                            quit()
                        else:
                            raise ValueError
                    except ValueError:
                        print(f"""{Fore.CYAN}
    Please select 'y' or 'n' only""")
            elif instr_choice == 2:
                return
            else:
                raise ValueError
        except ValueError:
            print(f"""{Fore.CYAN}
    Please select '1' or '2' only""")


user = enter_user_name()
show_instructions()


def main():
    scores = SHEET.worksheet('scores')

    all_data = scores.get_all_values()
    scores_worksheet = SHEET.worksheet('scores')

    def how_many_rounds():
        """
        Function to select how many rounds a user wants to play in one game
        """
        while True:
            try:
                number_of_rounds = int(input(f"""{Fore.WHITE}
    How many rounds would you like to play (max 8)?: {Fore.YELLOW}"""))
                if 1 <= number_of_rounds <= 8:
                    print(f"""{Fore.WHITE}
        You selected {Fore.GREEN}{number_of_rounds} \
{Fore.WHITE}round(s)\n""")
                    break
                else:
                    raise ValueError
            except ValueError:
                print(f"""
    {Fore.CYAN}Please enter a number between 1 and 8""")
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
                print(f"""
    {Fore.WHITE}-----------------------------------------------------
    {Fore.WHITE}Round {increment}""")
                # Allow correct values with capital letters and spaces
                user_choice = input(f"""
    {Fore.WHITE}What's your choice? (rock, paper, scissors): \
{Fore.YELLOW}""").lower().strip()
                computer_choice = random.choice(options)
                if user_choice not in options:
                    print(f"""
    {Fore.RED}{user_choice} is not an option""")
                    continue
                else:
                    break
            print(f"""\n
    {Fore.WHITE}{user}'s choice: {Fore.GREEN}{user_choice}""")
            print(f"""
    {Fore.WHITE}Computer's choice: {Fore.CYAN}{computer_choice}""")
            if user_choice == computer_choice:
                print(f"""
    {Fore.YELLOW}Tie""")
            if (user_choice == 'rock' and computer_choice == 'scissors') \
                    or (user_choice == 'paper' and computer_choice == 'rock') \
                    or \
                    (user_choice == 'scissors' and computer_choice == 'paper'):
                user_score += 1
                if user_choice == 'rock' and computer_choice == 'scissors':
                    print(f"""
    {Fore.GREEN}{user} smashes computer""")
                if user_choice == 'paper' and computer_choice == 'rock':
                    print(f"""
    {Fore.GREEN}{user} covers computer""")
                if user_choice == 'scissors' and computer_choice == 'paper':
                    print(f"""
    {Fore.GREEN}{user} cuts computer""")
            elif (user_choice == 'rock' and computer_choice == 'paper') \
                    or \
                    (user_choice == 'paper' and computer_choice == 'scissors')\
                    or \
                    (user_choice == 'scissors' and computer_choice == 'rock'):
                computer_score += 1
                if user_choice == 'rock' and computer_choice == 'paper':
                    print(f"""
    {Fore.RED}Computer covers {user}""")
                if user_choice == 'paper' and computer_choice == 'scissors':
                    print(f"""
    {Fore.RED}Computer cuts {user}""")
                if user_choice == 'scissors' and computer_choice == 'rock':
                    print(f"""
    {Fore.RED}Computer smashes {user}""")
        return user_score, computer_score

    def display_score():
        """
        Final score is displayed and the winner announced
        """
        points = 0  # This variable will be used for updating the scores record
        print(f"""
    {Fore.WHITE}-----------------------------------------------------

    {Fore.CYAN}GAMEOVER

    {Fore.WHITE}{user} = {Fore.GREEN}{user_score}
    {Fore.WHITE}Computer = {Fore.CYAN}{computer_score}
    """)
        if user_score > computer_score:
            print(f"""

        {Fore.GREEN}{user} WINS! - YOU EARN 2 POINTS

        """)
            points = 2
        elif user_score < computer_score:
            print(f"""

        {Fore.RED}COMPUTER WINS! - YOU EARN 0 POINTS

         """)
            points = 0
        else:
            print(f"""

        {Fore.YELLOW}IT'S A TIE! - YOU EARN 1 POINT

        """)
            points = 1
        return points

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
                found = True
                """
                Calculate new values for the worksheet:
                add one to games played, add 'points' to points column,
                calculate new success rate"""
                games_played = int(name_row[1])
                games_played += 1
                points_total = int(name_row[2])
                new_points_total = points_total + points
                success_rate = round((new_points_total/(games_played*2))*100)
                new_name_row = \
                    [user, games_played, new_points_total, success_rate]
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
                print(f"""
    {Fore.CYAN}TO GET THE ACCURATE SUCCESS RATE ALWAYS UPDATE YOUR SCORE
    (GAME WON - 2 POINTS, TIE - 1 POINT, GAME LOST - 0 POINTS)""")
                add_score = input(f"""{Fore.WHITE}
    Would you like to add this score to your overall score record (y/n)? \
{Fore.YELLOW}""").lower()
                if add_score == 'y':
                    print(f"""
    {Fore.WHITE}Updating scores record...""")
                    found = False
                    for row in all_data:
                        if user in row:
                            found = True
                            """Find the cell where the existing name is
                            and convert the answer to a string"""
                            cell = scores_worksheet.find(user)
                            cell_string = str(cell)
                            # Remove the part up to the row number
                            split_cell = str(cell_string.split('<Cell R')[1])
                            # Remove the part from 'c' until the end.
                            # Return an integer with any number of digits
                            find_row_num = int(split_cell.rsplit('C')[0])
                            # Delete the existing row and add new row
                            scores_worksheet.delete_rows(find_row_num)
                            scores_worksheet.append_row(data)
                    if not found:
                        scores_worksheet.append_row(data)
                    print(f"""
    {Fore.WHITE}Scores worksheet updated successfully.""")
                    break
                elif add_score == 'n':
                    return
                else:
                    raise ValueError
            except ValueError:
                print(f"""
    {Fore.CYAN}Please select 'y' or 'n' only""")

    def display_overall_score():
        """
        Function to display current overall score from the google sheet
        """
        new_all_data = scores.get_all_values()
        found = False
        for row in new_all_data:
            if user in row:
                found = True
                # Get the headings from the scores worksheet's first row
                headings = SHEET.worksheet("scores").row_values(1)
                # Finding the row number where the values are
                cell = scores_worksheet.find(user)
                cell_string = str(cell)
                split_cell = str(cell_string.split('<Cell R')[1])
                find_row_num = int(split_cell.rsplit('C')[0])
                row_with_score = \
                    SHEET.worksheet("scores").row_values(find_row_num)
                i = 1
                # Printing the overall score
                print(f"""

        {Fore.MAGENTA}---------------------------
        {Fore.WHITE}{user}'s overall score is:
        {Fore.MAGENTA}---------------------------""")
                while i < 3:
                    print(f"""
        {headings[i]}: {Fore.GREEN}{row_with_score[i]}""")
                    i += 1
                print(f"""
        {Fore.WHITE}Success Rate: {Fore.GREEN}{row_with_score[3]}%
        {Fore.MAGENTA}---------------------------\n""")
        if not found:
            return

    points = display_score()
    new_overall_score = calculate_new_score_row()
    updated_score = update_scores_record(new_overall_score)
    display_overall_score()
    while True:
        try:
            play_again = input(f"""
    {Fore.WHITE}Would you like to play again (y/n): {Fore.YELLOW}""").lower()
            if play_again == 'y':
                main()
            elif play_again == 'n':
                print(f"""
    {Fore.WHITE}Thank you for playing, {Fore.GREEN}{user}
    {Fore.WHITE}Bye!""")
                quit()
            else:
                raise ValueError
        except ValueError:
            print(f"""{Fore.CYAN}
    Please select 'y' or 'n' only""")
            continue


main()
