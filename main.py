import time
import random
import threading
import os
from termcolor import colored
import smtplib
import csv

#
cardnum = 0
username = ""
money = 0
cash = 0
gambleticket = 0
#

print("")
print("what color would you like the system to be in other than: /playgame")
print(colored("red", 'red'))
print(colored("yellow", 'yellow'))
print(colored("green", 'green'))
print(colored("blue", 'blue'))
print(colored("magenta", "magenta"))
print("")
color = input("")


###_________======_________======_________======_________======_________###
###_________======_________======_________======_________======_________###

print("to access __BANKER__ system you must get a acount or sign in: type /get_acount or type /login")
system = input("")
if system == "/get_acount":
    first = random.randint(1, 9)
    first = str(first)
    n = 5

    nrs = [str(random.randrange(10)) for i in range(n - 1)]
    for i in range(len(nrs)):
        first += (nrs[i])

    print(colored("please enter email to verify human: ", color))
    email = input("")

    if "@" and "." in email:
        print(colored("checking if email is real...", color))
        time.sleep(0.9)
        print("")
    else:
        print(colored("incorect", color))
        time.sleep(0.5)
        print(colored("terminating code...", color))
        time.sleep(1)
        exit()

    server = smtplib.SMTP_SSL('smtp.gmail.com')
    server.login("bankingpythonservice@gmail.com", "04022010abc07914")
    server.sendmail("bankingpythonservice@gmail.com",
                    email,
                    str(first))

    print(colored("please enter the following pin that was sent to your email", color))
    enter = input("")

    if enter == (str(first)):
        print(colored("correct!", color))
        print(colored("you have got $500 dollars, GOOD JOB!", color))
        money = int(money) + 500
        print("your current money is", money)
        print("[THANK_YOU!]")
    else:
        print(colored("incorrect, sorry! ", color))
        exit()

    print("please enter a password: ")
    password = input("")
    print("saving file...")
    time.sleep(0.9)
    fileyay = open("user_name.txt", "a")
    fileyay.write(email)
    fileyay.close()
    #
    fileyay = open("password.txt", "a")
    fileyay.write(password)
    fileyay.close()

elif system == "/login":

    def cain():
        with open("user_name.txt", "r") as file:
            file_reader = csv.reader(file)
            user_find1(file_reader)
            file.close()

    def user_find1(file):
        user = input("Enter your email: ")
        for row in file:
            if row[0] == user:
                print("email found", user)
                user_found = [row[0]]
                break
            else:
                print(colored("email not found", color))
                exit()

    cain()

    def zain():
        with open("password.txt", "r") as file:
            file_reader = csv.reader(file)
            user_find1(file_reader)
            file.close()

    def user_find1(file):
        password = input("Enter your password: ")
        for row in file:
            if row[0] == password:
                print("password found", password)
                user_found = [row[0]]
                break
            else:
                print(colored("password not found", color))
                exit()

    zain()

else:
    print("L")
    exit()
################################################


file_size = os.stat('cardnum.txt').st_size

if file_size == 0:
    i = False
    print("The file is empty: " + str(file_size))
    print("")
else:
    i = True
    print("The file is not empty: " + str(file_size))

    def main():
        with open("cardnum.txt", "r") as file:
            file_reader = csv.reader(file)
            user_find(file_reader)
            file.close()

    def user_find(file):
        user = input("Enter your cardnum: ")
        for row in file:
            if row[0] == user:
                print(colored("cardnum found", user, color))
                user_found = [row[0]]
                break
            else:
                print(colored("cardnum not found", color))
                exit()

    main()
    yaya = open("money.txt", "r")
    print("current money:")
    fmoney = int(yaya.read())
    money = int(money) + int(fmoney)
    print(money)
    yaya.close()


#----------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
def playgame():
    name = input("what is your name: ")
    print("hello", (name))
    user = int(input("enter 1 for person vs person enter 2 for person vs ai: "))

    if user == 1:
        def display_board(board):
            blankBoard = """
        ___________________
        |     |     |     |
        |  7  |  8  |  9  |
        |     |     |     |
        |-----------------|
        |     |     |     |
        |  4  |  5  |  6  |
        |     |     |     |
        |-----------------|
        |     |     |     |
        |  1  |  2  |  3  |
        |     |     |     |
        |-----------------|
        """

            for i in range(1, 10):
                if (board[i] == 'O' or board[i] == 'X'):
                    blankBoard = blankBoard.replace(str(i), board[i])
                else:
                    blankBoard = blankBoard.replace(str(i), ' ')
            print(blankBoard)

        def player_input():
            player1 = input(colored("Please pick a marker 'X' or 'O' ", color))
            while True:
                if player1.upper() == 'X':
                    player2 = 'O'
                    print("You've choosen " + player1 + ". Player 2 will be " + player2)
                    return player1.upper(), player2
                elif player1.upper() == 'O':
                    player2 = 'X'
                    print("You've choosen " + player1 + ". Player 2 will be " + player2)
                    return player1.upper(), player2
                else:
                    player1 = input("Please pick a marker 'X' or 'O' ")

        def place_marker(board, marker, position):
            board[position] = marker
            return board

        def space_check(board, position):
            return board[position] == '#'

        def full_board_check(board):
            return len([x for x in board if x == '#']) == 1

        def win_check(board, mark):
            if board[1] == board[2] == board[3] == mark:
                return True
            if board[4] == board[5] == board[6] == mark:
                return True
            if board[7] == board[8] == board[9] == mark:
                return True
            if board[1] == board[4] == board[7] == mark:
                return True
            if board[2] == board[5] == board[8] == mark:
                return True
            if board[3] == board[6] == board[9] == mark:
                return True
            if board[1] == board[5] == board[9] == mark:
                return True
            if board[3] == board[5] == board[7] == mark:
                return True
            return False

        def player_choice(board):
            choice = input("Please select an empty space between 1 and 9 : ")
            while not space_check(board, int(choice)):
                choice = input("This space isn't free. Please choose between 1 and 9 : ")
            return choice

        if __name__ == "__main__":
            print('Welcome to Tic Tac Toe!')
            i = 1
            players = player_input()
            board = ['#'] * 10
            while True:

                game_on = full_board_check(board)
                while not game_on:
                    position = player_choice(board)
                    if i % 2 == 0:
                        marker = players[1]
                    else:
                        marker = players[0]
                    # Play!
                    place_marker(board, marker, int(position))
                    # Check the board
                    display_board(board)
                    i += 1
                    if win_check(board, marker):
                        print("You won !")

                    game_on = full_board_check(board)


                else:
                    i = 1
                    players = player_input()
                    board = ['#'] * 10
    elif user == 2:
        print("|")
        time.sleep(0.5)
        print("/")

        board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

        def TICTACTOE():
            print((colored(
                """
             _____  _  ____     _____  ____  ____     _____  ____  _____
            /__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/    
              / \  | ||  / |   | / \  | / \||  / __  _ / \  | / \||  \      
              | |  | ||  \_\_   _\| |  | |-|||  \_\  _\| |  | \_/||  /_     
              \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____\



            """, 'yellow')))

        def print_board():
            print(colored('tic tac toe', 'red'), colored('world', 'green'))
            print(colored(" ", 'red'))
            print(colored("   |   |   ", 'blue'))
            print(colored(" " + board[1] + " | " + board[2] + " | " + board[3] + "  ", 'red'))
            print(colored("   |   |   ", 'yellow'))
            print(colored("---|---|---", 'blue'))
            print(colored("   |   |   ", 'red'))
            print(colored(" " + board[4] + " | " + board[5] + " | " + board[6] + "  ", 'yellow'))
            print(colored("   |   |   ", 'blue'))
            print(colored("---|---|---", 'red'))
            print(colored("   |   |   ", 'yellow'))
            print(colored(" " + board[7] + " | " + board[8] + " | " + board[9] + "  ", 'blue'))
            print(colored("   |   |   ", 'red'))

        def winnerwinnerchickendinner(board, player):
            if (board[1] == player and board[2] == player and board[3] == player) or \
                    (board[4] == player and board[5] == player and board[6] == player) or \
                    (board[7] == player and board[8] == player and board[9] == player) or \
                    (board[1] == player and board[4] == player and board[7] == player) or \
                    (board[2] == player and board[5] == player and board[8] == player) or \
                    (board[3] == player and board[6] == player and board[9] == player) or \
                    (board[1] == player and board[5] == player and board[9] == player) or \
                    (board[3] == player and board[5] == player and board[7] == player):
                return True
            else:
                return False

        def is_board_full(board):
            if " " in board:
                return False
            else:
                return True

        def ai_move(board, player):
            if board[5] == " ":
                print("the AI is THINKING...")
                time.sleep(1)
                return 5

            while True:
                move = random.randint(1, 9)
                if board[move] == " ":
                    print("the AI is THINKING...")
                    time.sleep(0.9)
                    return move
                    break

            return 5

        while True:
            os.system("cls")
            TICTACTOE()
            print_board()

            choice = input(colored("Please choose an empty space for X. ", 'green'))
            choice = int(choice)

            if board[choice] == " ":
                board[choice] = "X"
            else:
                print("Sorry, that space is not empty")
                time.sleep(1)

            if winnerwinnerchickendinner(board, "X"):
                os.system("cls")
                TICTACTOE()
                print_board()
                print(colored("X wins! Congratulations", 'blue'))
                break

            os.system("cls")
            print_board()

            if is_board_full(board):
                print("Tie!")
                break

            choice = ai_move(board, "O")
            #
            if board[choice] == " ":
                board[choice] = "O"
            else:
                print
                "Sorry, that space is not empty!"
                time.sleep(1)

            if winnerwinnerchickendinner(board, "O"):
                os.system("cls")
                TICTACTOE()
                print_board()
                print(colored("O wins! Congratulations" 'red'))
                break

            if is_board_full(board):
                print("Tie!")
                break
    else:
        print("tinkering with system is not accepted")
        exit()

print(colored("          _____                    _____                    _____                    _____                    _____                    _____ ", 'red'))
print(colored("         /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \ ", 'red'))
print(colored("        /::\    \                /::\    \                /::\____\                /::\____\                /::\    \                /::\    \  ", 'red'))
print(colored("       /::::\    \              /::::\    \              /::::|   |               /:::/    /               /::::\    \              /::::\    \ ", 'red'))
print(colored("      /::::::\    \            /::::::\    \            /:::::|   |              /:::/    /               /::::::\    \            /::::::\    \  ", 'red'))
print(colored("     /:::/\:::\    \          /:::/\:::\    \          /::::::|   |             /:::/    /               /:::/\:::\    \          /:::/\:::\    \ ", 'red'))
print(colored("    /:::/__\:::\    \        /:::/__\:::\    \        /:::/|::|   |            /:::/____/               /:::/__\:::\    \        /:::/__\:::\    \  ", 'yellow'))
print(colored("   /::::\   \:::\    \      /::::\   \:::\    \      /:::/ |::|   |           /::::\    \              /::::\   \:::\    \      /::::\   \:::\    \  ", 'yellow'))
print(colored("  /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/  |::|   | _____    /::::::\____\________    /::::::\   \:::\    \    /::::::\   \:::\    \ ", 'yellow'))
print(colored(" /:::/\:::\   \:::\ ___\  /:::/\:::\   \:::\    \  /:::/   |::|   |/\    \  /:::/\:::::::::::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\ ", 'yellow'))
print(colored("/:::/__\:::\   \:::|    |/:::/  \:::\   \:::\____\/:: /    |::|   /::\____\/:::/  |:::::::::::\____\/:::/__\:::\   \:::\____\/:::/  \:::\   \:::|    | ", 'yellow'))
print(colored("\:::\   \:::\  /:::|____|\::/    \:::\  /:::/    /\::/    /|::|  /:::/    /\::/   |::|~~~|~~~~~     \:::\   \:::\   \::/    /\::/   |::::\  /:::|____| ", 'green'))
print(colored(" \:::\   \:::\/:::/    /  \/____/ \:::\/:::/    /  \/____/ |::| /:::/    /  \/____|::|   |           \:::\   \:::\   \/____/  \/____|:::::\/:::/    / ", 'green'))
print(colored("  \:::\   \::::::/    /            \::::::/    /           |::|/:::/    /         |::|   |            \:::\   \:::\    \            |:::::::::/    / ", 'green'))
print(colored("   \:::\   \::::/    /              \::::/    /            |::::::/    /          |::|   |             \:::\   \:::\____\           |::|\::::/    / ", 'green'))
print(colored("    \:::\  /:::/    /               /:::/    /             |:::::/    /           |::|   |              \:::\   \::/    /           |::| \::/____/ ", 'blue'))
print(colored("     \:::\/:::/    /               /:::/    /              |::::/    /            |::|   |               \:::\   \/____/            |::|  ~| ", 'blue'))
print(colored("      \::::::/    /               /:::/    /               /:::/    /             |::|   |                \:::\    \                |::|   | ", 'blue'))
print(colored("       \::::/    /               /:::/    /               /:::/    /              \::|   |                 \:::\____\               \::|   | ", 'blue'))
print(colored("        \::/____/                \::/____/                \::/____/                \:|---|                  \::/____/                \:|___| ", 'blue'))

print(colored("""_________________________________________""", 'red'), colored("""_________________________________________""", 'yellow'), colored("""_________________________________________""", 'green'), colored("""_________________________________________""", 'blue'))

if i == False:
    print(colored("you have a choice to take any credit card you want. just type in the correct bank company in the correct "
          "spelling and you will be able to use that card that was given for tasks", color))
    print(colored("chase, disneyclub, visa13, or visa16 ", color))
    creditcardchoice = input("")
    if creditcardchoice == "visa16":
        a1 = random.randint(0, 9)
        a2 = random.randint(0, 9)
        a3 = random.randint(0, 9)
        a4 = random.randint(0, 9)
        a5 = random.randint(0, 9)
        a6 = random.randint(0, 9)
        a7 = random.randint(0, 9)
        a8 = random.randint(0, 9)
        a9 = random.randint(0, 9)
        a10 = random.randint(0, 9)
        a11 = random.randint(0, 9)
        a12 = random.randint(0, 9)
        a13 = random.randint(0, 9)
        a14 = random.randint(0, 9)
        a15 = random.randint(0, 9)
        a16 = random.randint(0, 9)
        print(colored("VISA16", color))
        print(a1, a2, a3, a4, ' ', a5, a6, a7, a8, ' ', a9, a10, a11, a12, ' ', a13, a14, a15, a16)
        print(colored("please copy and paste the credit card info into the folliwing message box ", color))
        print(colored("if the credit card info is not the same then there will be issues", color))
        cardnum = input("")
        print(colored(cardnum, color))
        print(colored('since you joined our banking system, we will give you $5000 0% intrest ', color))
        money = int(money) + 5000
        print('your money so far is, ', '$', money)
        print(" ")
        print(" ")
    elif creditcardchoice == "visa13":
        b1 = random.randint(0, 9)
        b2 = random.randint(0, 9)
        b3 = random.randint(0, 9)
        b4 = random.randint(0, 9)
        b5 = random.randint(0, 9)
        b6 = random.randint(0, 9)
        b7 = random.randint(0, 9)
        b8 = random.randint(0, 9)
        b9 = random.randint(0, 9)
        b10 = random.randint(0, 9)
        b11 = random.randint(0, 9)
        b12 = random.randint(0, 9)
        b13 = random.randint(0, 9)
        print(colored("VISA13", color))
        print(b1, b2, b3, b4, ' ', b5, b6, b7, b8, ' ', b9, b10, b11, b12, b13)
        print(colored("please copy and paste the credit card info into the folliwing message box ", color))
        print(colored("if the credit card info is not the same then there will be issues", color))
        cardnum = input("")
        print(colored(cardnum, color))
        print(colored('since you joined our banking system, we will give you $5000 0% intrest ', color))
        money = int(money) + 5000
        print('your money so far is, ', '$', money)
        print(" ")
        print(" ")

    elif creditcardchoice == "disneyclub":
        b1 = random.randint(0, 9)
        b2 = random.randint(0, 9)
        b3 = random.randint(0, 9)
        b4 = random.randint(0, 9)
        b5 = random.randint(0, 9)
        b6 = random.randint(0, 9)
        b7 = random.randint(0, 9)
        b8 = random.randint(0, 9)
        b9 = random.randint(0, 9)
        b10 = random.randint(0, 9)
        b11 = random.randint(0, 9)
        b12 = random.randint(0, 9)
        print(colored("DISNEYCLUB", color))
        print(b1, b2, b3, b4, ' ', b5, b6, b7, b8, ' ', b9, b10, b11, b12)
        print(colored("please copy and paste the credit card info into the folliwing message box ", color))
        print(colored("if the credit card info is not the same then there will be issues", color))
        cardnum = input("")
        print(colored(cardnum, color))
        print(colored('since you joined our banking system, we will give you $5000 0% intrest ', color))
        money = int(money) + 5000
        print('your money so far is, ', '$', money)
        print(" ")
        print(" ")
    elif creditcardchoice == "chase":
        a1 = random.randint(0, 9)
        a2 = random.randint(0, 9)
        a3 = random.randint(0, 9)
        a4 = random.randint(0, 9)
        a5 = random.randint(0, 9)
        a6 = random.randint(0, 9)
        a7 = random.randint(0, 9)
        a8 = random.randint(0, 9)
        a9 = random.randint(0, 9)
        a10 = random.randint(0, 9)
        a11 = random.randint(0, 9)
        a12 = random.randint(0, 9)
        a13 = random.randint(0, 9)
        a14 = random.randint(0, 9)
        a15 = random.randint(0, 9)
        a16 = random.randint(0, 9)
        print(colored("CHASE", color))
        print(a1, a2, a3, a4, ' ', a5, a6, a7, a8, ' ', a9, a10, a11, a12, ' ', a13, a14, a15, a16)
        print(colored("please copy and paste the credit card info into the folliwing message box ", color))
        print(colored("if the credit card info is not the same then there will be issues", color))
        cardnum = input("")
        print(colored(cardnum, color))
        print(colored('since you joined our banking system, we will give you $5000 0% intrest ', color))
        money = int(money) + 5000
        print('your money so far is, ', '$', money)
        print(" ")
        print(" ")

    print("saving file...")
    time.sleep(0.9)
    file1 = open("cardnum.txt", "w")
    file1.write(cardnum)
    file1.close()
    file1 = open("money.txt", "w")
    file1.write(str(money))
    file1.close()

def help():
    print(colored("type /calculater to calculate whatever of your liking", color))
    print(colored("type /withdraw to take out money from your acount", color))
    print(colored("type /deposite to deposite cash so you can put it into your bank account", color))
    print(colored("type /job to join a job to add to your card", color))
    print(colored("type /bank_money to print out how much money you have ", color))
    print(colored("type /cash to show how much cash you have ", color))
    print(colored("type /playgame to take a break and play tic-tac-toe with a friend or bot!", color))
    print(colored("type /rewards_center to get free money without a job!", color))
    print(colored("type /store to buy things with your money", color))
    print(colored("type /gamble to gamble but you need to buy a gamble ticket from the store or else program withh crash", color))
    print(" ")
    print(" ")
    print(" ")
def calculater():
    print(colored("calculater for eternal banking", color))
    print(colored("enter add, sub, division, multiplication, modulus, or exponent: ", color))
    calc = input("")
    if calc == "add":
        add = int(input(colored('enter number one: ', color)))
        add2 = int(input(colored('enter number two: ', color)))
        ans = add + add2
        print(colored(ans, color))
    elif calc == "sub":
        sub = int(input(colored('enter number one: ', color)))
        sub2 = int(input(colored('enter number two: ', color)))
        ans = sub - sub2
        print(colored(ans, color))
    elif calc == "division":
        division = int(input(colored('enter number one: ', color)))
        division2 = int(input(colored('enter number two: ', color)))
        ans = division / division2
        print(colored(ans, color))
    elif calc == "multiplication":
        multiplication = int(input(colored('enter number one: ', color)))
        multiplication2 = int(input(colored('enter number two: ', color)))
        ans = multiplication * multiplication2
        print(colored(ans, color))
    elif calc == "modulus":
        modulus = int(input(colored('enter number one: ', color)))
        modulus2 = int(input(colored('enter number two: ', color)))
        ans = modulus % modulus2
        print(colored(ans, color))
    if calc == "exponent":
        exponent = int(input(colored('enter number one: ', color)))
        exponent2 = int(input(colored('enter number two: ', color)))
        ans = exponent ** exponent2
        print(colored(ans, color))

print(colored("welcome to the eternal banking, please enter command of your choice ", color))
print(colored("please enter /help to show all commands ", color))
print(colored("or you can enter !quit to quit the program", color))
print(colored("want a break? well type /playgame for tictactoe!", color))
choice = input("")

while choice != "!quit":

    if choice == "/playgame":
        playgame()
    elif choice == "/help":
        help()
    elif choice == "/calculater":
        calculater()

    elif choice == "/bank_money":
        print("you currently have: ", "$", money, "in bank acount")

    elif choice == "/cash":
        print("you currently have: ", "$", cash, "in cash")

    elif choice == "/job":
        print(colored("please enter your valid credit card", color))
        jobcard = input("")
        while jobcard == cardnum:
            if jobcard == cardnum:
                print(colored("correct", color))
            else:
                print(colored("invalid input please try again", color))
            jobcard = input(colored("please press 0-enter to proceed: ", color))
        print(colored("solve math questions to make money. type math to start. type anything else to quit", color))
        jobchoice = input("")
        if jobchoice == "math":
            print(colored("cool", color))
            print(colored("please type how many questions you want? if you want to quit right now, type 0", color))
            apple = int(input(''))
            score = 0
            for i in range(apple):
                symbol = random.randint(1, 4)

                if symbol == 1:
                    num1 = random.randint(1, 100)
                    num2 = random.randint(1, 100)
                    question = int(input(colored("What is " + str(num1) + "+" + str(num2) + "?: ", color)))
                    answer = num1 + num2
                    if question == answer:
                        print("good job")
                        cash = cash + 50
                        print(colored("you get 50 dollars in cash, HOORAY", 'green'))
                        print(" ")
                        print(" ")
                        print('your current cash is   ', '$', cash)
                    else:
                        print(colored("wrong, you lose 20 dollars in cash, sorry.", 'red'))
                        print(" ")
                        print(" ")
                        cash = cash - 20
                        print('your current cash is   ', '$', cash)
                elif symbol == 2:
                    num5 = random.randint(1, 12)
                    num6 = random.randint(1, 14)
                    question = int(input(colored("What is " + str(num5) + "*" + str(num6) + "?: ", color)))
                    answer = num5 * num6
                    if question == answer:
                        print("good job")
                        cash = cash + 50
                        print(colored("you get 50 dollars in cash, HOORAY", 'green'))
                        print('your current cash is   ', '$', cash)
                        print(" ")
                        print(" ")
                    else:
                        print(colored("wrong, you lose 20 dollars in cash, sorry.", 'red'))
                        print(" ")
                        print(" ")
                        cash = cash - 20
                        print('your current cash is   ', '$', cash)
                elif symbol == 3:
                    num7 = random.randint(1, 10)
                    num8 = random.randint(1, 10)
                    question = int(input(colored("What is " + str(num7) + "^" + str(num8) + "?: ", color)))
                    answer = num7 ** num8
                    if question == answer:
                        print("good job")
                        cash = cash + 50
                        print(colored("you get 50 dollars in cash, HOORAY", 'green'))
                        print('your current cash is   ', '$', cash)
                        print(" ")
                        print(" ")
                    else:
                        print(colored("wrong, you lose 20 dollars in cash, sorry.", 'red'))
                        print(" ")
                        print(" ")
                        cash = cash - 20
                        print('your current cash is   ', '$', cash)
                elif symbol == 4:
                    num9 = random.randint(1, 36)
                    num10 = random.randint(1, 12)
                    question = int(input(colored("What is " + str(num9) + "%" + str(num10) + "?: ", color)))
                    answer = num9 % num10
                    if question == answer:
                        print("good job")
                        cash = cash + 50
                        print(colored("you get 50 dollars in cash, HOORAY", 'green'))
                        print('your current cash is   ', '$', cash)
                        print(" ")
                        print(" ")
                    else:
                        print(colored("wrong, you lose 20 dollars in cash, sorry.", 'red'))
                        print(" ")
                        print(" ")
                        cash = cash - 20
                        print('your current cash is   ', '$', cash)
            print("when you want to receive the money type /deposit")
            print(" ")
            print(" ")

    elif choice == "/rewards_center":
        print(colored("please enter your valid credit card", color))
        surveycard = input("")
        while surveycard == cardnum:
            if surveycard == cardnum:
                print(colored("correct", color))
            else:
                print(colored("invalid input please try again", color))
            surveycard = input(colored("please press 0-enter to proceed: ", color))
        print(colored("please type /rewards to enter the rewards center ", color))
        jobchoice = input("")
        if surveycard == "/rewards":
            print(" ")
            print(colored("you can receive money from the rewards center from: doing surveys, verifying email", color))
            print(colored("/survey for $1000 or /verify_email for $500", color))
            print(colored("if you would like to exit rewards center then type /exit_rewards", color))
            rewardschoice = input("")
            while rewardschoice != "/exit_rewards":
                if rewardschoice == "/verify_email":
                    first = random.randint(1, 9)
                    first = str(first)
                    n = 5

                    nrs = [str(random.randrange(10)) for i in range(n - 1)]
                    for i in range(len(nrs)):
                        first += (nrs[i])

                    print(colored("please enter email to verify human: ", color))
                    email = input("")

                    if "@" and "." in email:
                        print(colored("checking if email is real...", color))
                        time.sleep(0.9)
                        print("")
                    else:
                        print(colored("incorect", color))
                        time.sleep(0.5)
                        print(colored("terminating code...", color))
                        time.sleep(1)
                        exit()

                    server = smtplib.SMTP_SSL('smtp.gmail.com')
                    server.login("bankingpythonservice@gmail.com", "04022010abc07914")
                    server.sendmail("bankingpythonservice@gmail.com",
                                    email,
                                    str(first))

                    print(colored("please enter the following pin that was sent to your email", color))
                    enter = input("")

                    if enter == (str(first)):
                        print(colored("correct!", color))
                        print(colored("you have got $500 dollars, GOOD JOB!", color))
                        money = int(money) + 500
                        print("your current money is", money)
                        break
                    else:
                        print(colored("incorrect, sorry! ", color))
                        exit()
                elif rewardschoice == "/survey":
                    print(colored(
                        "you will be granted $1000 if you PASS (90 points) the common knowledge test. "
                        "solve as many questions in 30 "
                        "seconds", color))
                    print(" ")
                    print(colored("starting the test in 7 seconds", color))
                    time.sleep(7)


                    def countdown():
                        global timer
                        timer = 60

                        for x in range(60):
                            timer = timer - 1
                            time.sleep(1)
                        print(colored("out of time", color))


                    countdownthread = threading.Thread(target=countdown)
                    countdownthread.start()
                    points = 0
                    ok = 0
                    while timer > 0:
                        print(colored("1. what is the 5th planet from the sun?", color))
                        print(colored("type the correct the letter that you think the answer is on", color))
                        print(colored("(a): Earth", color))
                        print(colored("(b): Jupiter", color))
                        print(colored("(c): Uranus", color))
                        print(colored("(d): Mars", color))
                        q1 = input("")
                        if q1 == "b":
                            print(colored("correct", color))
                            points = int(points) + 10
                            print("your current points are,", points)
                            ok = int(ok) + 1
                        else:
                            print(colored("incorrect", color))
                            ok = int(ok) + 1
                        print(" ")
                        print(" ")
                        print(colored("2. What's the biggest animal in the world?", color))
                        print(colored("(a): blue whale", color))
                        print(colored("(b): elephant", color))
                        print(colored("(c): gorilla", color))
                        print(colored("(d): Giraffe", color))
                        q2 = input("")
                        if q2 == "a":
                            print(colored("correct", color))
                            points = int(points) + 10
                            print("your current points are,", points)
                            ok = int(ok) + 1
                        else:
                            print(colored("incorrect", color))
                            ok = int(ok) + 1
                        print(" ")
                        print(" ")
                        print(colored("What is the largest country in the world?", color))
                        print(colored("(a): USA", color))
                        print(colored("(b): Canada", color))
                        print(colored("(c): China", color))
                        print(colored("(d): russia", color))
                        q3 = input("")
                        if q3 == "d":
                            print(colored("correct", color))
                            points = int(points) + 10
                            print("your current points are,", points)
                            ok = int(ok) + 1
                        else:
                            print(colored("incorrect", color))
                            ok = int(ok) + 1
                        print(" ")
                        print(" ")
                        print(colored("How many elements are there in the periodic table?", color))
                        print(colored("(a): 67", color))
                        print(colored("(b): 56", color))
                        print(colored("(c) 118", color))
                        print(colored("(d): 12", color))
                        q4 = input("")
                        if q4 == "c":
                            print(colored("correct", color))
                            points = int(points) + 10
                            print("your current points are,", points)
                            ok = int(ok) + 1
                        else:
                            print(colored("incorrect", color))
                            ok = int(ok) + 1
                        print(" ")
                        print(" ")
                        print(colored("Who is the president of the United states in 2021", color))
                        print(colored("(a): Donald Trump", color))
                        print(colored("(b): George Bush", color))
                        print(colored("(c): Joe Biden", color))
                        print(colored("(d): Barack Obama", color))
                        q5 = input("")
                        if q5 == "c":
                            print(colored("correct", color))
                            points = int(points) + 10
                            print("your current points are,", points)
                            ok = int(ok) + 1
                        else:
                            print(colored("incorrect", color))
                            ok = int(ok) + 1
                        print(" ")
                        print(" ")
                        print(colored("is Covid-19 airborn? true of false", color))
                        print(colored("(t) true", color))
                        print(colored("(f) false", color))
                        q6 = input("")
                        if q6 == "t":
                            print(colored("correct", color))
                            points = int(points) + 10
                            print("your current points are,", points)
                            ok = int(ok) + 1
                        else:
                            print(colored("incorrect", color))
                            ok = int(ok) + 1
                        print(" ")
                        print(" ")
                        print(colored("What is the largest insect that ever lived?", color))
                        print(colored("(a): Giant wētā", color))
                        print(colored("(b): Goliath Beetle", color))
                        print(colored("(c): Atlas Moth", color))
                        print(colored("(d): Tarantula Hawk", color))
                        q7 = input("")
                        if q7 == "a":
                            print(colored("correct", color))
                            points = int(points) + 10
                            print("your current points are,", points)
                            ok = int(ok) + 1
                        else:
                            print(colored("incorrect", color))
                            ok = int(ok) + 1
                        print(" ")
                        print(" ")
                        print(colored("Does Mars have any signs of life as of 2021?", color))
                        print(colored("(a): There is no sign of life on Mars.", color))
                        print(colored("(b): Rovers have seen life on mars before.", color))
                        print(colored("(c): Mars used to have signs of life long ago.", color))
                        print(colored("(d): A rover found something that looks like signs of life but not sure", color))
                        q8 = input("")
                        if q8 == "a" or "d":
                            print(colored("correct", color))
                            points = int(points) + 10
                            print("your current points are,", points)
                            ok = int(ok) + 1
                        else:
                            print(colored("incorrect", color))
                            ok = int(ok) + 1
                        print(" ")
                        print(" ")
                        print("")
                        print(colored("Entomology is the science that studies- ", color))
                        print(colored("(a): Behavior of human beings", color))
                        print(colored("(b): Insects", color))
                        print(colored("(c): The origin and history of technical and scientific terms", color))
                        print(colored("(d): The formation of rocks", color))
                        q9 = input("")
                        if q9 == "b":
                            print(colored("correct", color))
                            points = int(points) + 10
                            print("your current points are,", points)
                            ok = int(ok) + 1
                        else:
                            print(colored("incorrect", color))
                            ok = int(ok) + 1
                        print(" ")
                        print(" ")
                        print(colored("For which of the following disciplines is Nobel Prize awarded?", color))
                        print(colored("(a): Physics and Chemistry", color))
                        print(colored("(b): Physiology or Medicine", color))
                        print(colored("(c): Literature, Peace and Economics", color))
                        print(colored("(d): All of the above", color))
                        q10 = input("")
                        if q10 == "d":
                            print(colored("correct", color))
                            points = int(points) + 10
                            print("your current points are,", points)
                            ok = int(ok) + 1
                        else:
                            print(colored("incorrect", color))
                            ok = int(ok) + 1
                        if int(points) >= 90:
                            money = int(money) + 1000
                        if int(ok) >= 10:
                            break
                    break
            print(colored("good job, money will be added or lost", color))
            print(" ")
            print(" ")
            print(colored("you can receive money from the rewards center from: doing surveys, verifying phone", color))
            print(colored("/survey or /verify_phone"))
            print(colored("if you would like to exit rewards center then type /exit_rewards", color))
            rewardschoice = input("")

    elif choice == "/withdraw":
        print(" ")
        print(colored("you currently have: ", "$", money, "in bank acount", color))
        print(colored("you currently have: ", "$", cash, "in cash", color))
        print(colored("how much money would you like to withdraw?", color))
        withdrawamount = int(input(""))
        money = money - withdrawamount
        cash = cash + withdrawamount
        print(colored("you currently have: ", "$", money, "in bank acount", color))
        print(colored("you currently have: ", "$", cash, "in cash", color))
        print(" ")


    elif choice == "/deposit":
        print(" ")
        print("you currently have: ", "$", money, "in bank acount")
        print("you currently have: ", "$", cash, "in cash")
        print(colored("how much money would you like to deposit?", color))
        withdrawamount = int(input(""))
        money = money + withdrawamount
        cash = cash - withdrawamount
        print("you currently have: ", "$", money, "in bank acount")
        print("you currently have: ", "$", cash, "in cash")
        print(" ")

    elif choice == "/store":
        print("")
        print(colored("you can buy a gamble ticket for: $525, /GAMBLE_TICKET", color))
        print(colored("you can buy a cheat code for 4000, /cheat_code", color))
        storechoice = input("")
        if storechoice == "/GAMBLE_TICKET":
            money = int(money) - 525
            gambleticket = int(gambleticket) + 1
            print('you have:',money, "in your bank acount" )
            print('you have:',gambleticket,'gambling ticket(s)')
            print("")
        if storechoice == "/cheat_code":
                cheat = random.randint(1, 1)
                print(colored("you have lost 4000 dollars", color))
                money = int(money) - 4000
                print('you have $', money, 'money in your bank acount left')
                print(colored("finding scrap codes...", color))
                time.sleep(0.9)
                print("cheat found!")
                if int(cheat) == 1:
                    print(colored("you have unlocked money_hack^43 ", color))
                    print(colored("you get 10000 dollars", color))
                    money = int(money) + 10000
                    print('you have $', money, 'money in your bank acount')
                    print(colored("happy days!", color))
                    print("")
                    print("")

    elif choice == "/gamble":
        if gambleticket >= 1:
            print(colored("you have used one of your gamble tickets", color))
            gambleticket = int(gambleticket) - gambleticket
            print('you have:', gambleticket, 'gambling tickets left')
        elif gambleticket <= 0:
            print("tinkering with the system is unaccepcepted")
            print(colored("gambled ticket == 0", color))
            exit()
        print(colored("please enter how much money you would like to bet: ", color))
        how_much = input('')
        money = int(money) - int(how_much)
        print("great money has been subtracted to gamble, your current money is:", money)
        print("")
        # ==============================================================================================================#
        print(colored("you will be playing a 3 color roulette", color))
        print(colored("black = 2x cashout (common)", color))
        print(colored("red = 3x cashout [(uncommon)]", color))
        print(colored("white is 5x cashout {(rare)} ", color))
        print(colored("green = 12x cashout |[(LEGENDARY)]|", color))
        print(colored("enter ///quit to exit to the main page", color))
        color_choice = input("")
        roll = random.randint(1, 19)
        print(colored("generating_number...", color))
        time.sleep(0.5)
        print(roll)

        while color_choice != "///quit":
            if roll <= 10:
                print(colored("black", color))
                if color_choice == "black":
                    print(colored("correct money will be added", color))
                    how_much = int(how_much) * 2
                    money = money + how_much
                    print("your current money is:", money)
                    print("")
                else:
                    print(colored("sorry incorrect, no money will be added", color))
                    print("your current money is:", money)
                    print("")

            elif roll <= 15 and roll >= 11:
                print("red")
                if color_choice == "red":
                    print(colored("correct money will be added", color))
                    how_much = int(how_much) * 3
                    money = money + how_much
                    print("your current money is:", money)
                    print("")
                else:
                    print(colored("sorry incorrect, no money will be added", color))
                    print("your current money is:", money)
                    print("")

            elif roll <= 18 and roll >= 16:
                print("white")
                if color_choice == "white":
                    print(colored("correct money will be added", color))
                    how_much = int(how_much) * 5
                    money = money + how_much
                    print("your current money is:", money)
                    print("")
                else:
                    print(colored("sorry incorrect, no money will be added", color))
                    print("your current money is:", money)
                    print("")

            elif roll == 19:
                print("green")
                if color_choice == "green":
                    print(colored("correct money will be added", color))
                    how_much = int(how_much) * 12
                    money = money + how_much
                    print("your current money is:", money)
                    print("")
                else:
                    print(colored("sorry incorrect, no money will be added", color))
                    print("your current money is:", money)
                    print("")
            print(colored("please enter how much money you would like to bet: ", color))
            how_much = input('')
            money = int(money) - int(how_much)
            print("great money has been subtracted to gamble, your current money is:", money)
            print("")

            print(colored("you will be playing a 3 color roulette", color))
            print(colored("black = 2x cashout (common)", color))
            print(colored("red = 3x cashout [(uncommon)]", color))
            print(colored("white is 5x cashout {(rare)} ", color))
            print(colored("green = 12x cashout |[(LEGENDARY)]|", color))
            print(colored("enter ///quit to exit to the main page", color))
            color_choice = input("")
            roll = random.randint(1, 19)
            print(colored("generating_number...", color))
            time.sleep(0.5)
            print(roll)

    print(colored("welcome to the eternal banking, please enter command of your choice ", color))
    print(colored("please enter /help to show all commands ", color))
    print(colored("or you can enter !quit to quit the program", color))
    print(colored("want a break? well type /playgame for tictactoe!", color))
    choice = input("")
print("saving file...")
time.sleep(0.9)
file1 = open("cardnum.txt", "w")
file1.write(cardnum)
file1.close()
file1 = open("money.txt", "w")
file1.write(str(money))
file1.close()
exit()