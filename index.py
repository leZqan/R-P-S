import random


def init():
    print("Welcome To Rock, Paper, Scissors")
    print(" Rock beats Scissors!!! \n Scissors beats Paper!!! \n Paper beats Rock!!!")
    computer_options = ["R", "P", "S"]
    cpu_move = random.choice(computer_options)
    if cpu_move == "R":
        cpu_move = "Rock"
    elif cpu_move == "P":
        cpu_move = "Paper"
    elif cpu_move == "S":
        cpu_move = "Scissors"

    while True:
        user_move = (
            input("Pick your move: R for Rock, P for Paper, S for Scissors \n ")).upper()
        if user_move == "R":
            user_move = "Rock"
            game(user_move, cpu_move)
            break
        elif user_move == "P":
            user_move = "Paper"
            game(user_move, cpu_move)
            break
        elif user_move == "S":
            user_move = "Scissors"
            game(user_move, cpu_move)
            break
        else:
            print("You have entered an invalid selection, Try again")


def game(user_move, cpu_move):
    print("== === == === == === ==")
    print("You picked: ", user_move)
    print("C.P.U picked: ", cpu_move)
    print("== === == === == === ==")
    if user_move == cpu_move:
        print(" TIE!!! ")
        init()
    elif user_move == "Rock":
        if cpu_move == "Scissors":
            print("You Win!!!")
        if cpu_move == "Paper":
            print("You Lose!!!")
    elif user_move == "Paper":
        if cpu_move == "Scissors":
            print("You Lose!!!")
        if cpu_move == "Rock":
            print("You Win!!!")

    elif user_move == "Scissors":
        if cpu_move == "Paper":
            print("You Win!!!")
        if cpu_move == "Rock":
            print("You Lose!!!")
    while True:
        print("== === == === == === ==")
        user_input = (input("Would You Like To Continue? YES/NO \n")).upper()
        if user_input == "YES":
            init()
        elif user_input == "NO":
            print("Thanks and Bye")
            exit()
        else:
            print("You've made an invalid selection, Try again.")


init()
