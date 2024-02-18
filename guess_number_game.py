import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
 
def difficulty():
    level=input("Choose a Difficulty level. EASY or HARD :")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def check(guess,answer,turns):
    if guess > answer:
        print("Attempt TOO HIGH !")
        return turns - 1
    elif guess < answer:
        print("Attempt TOO LOW !")
        return turns - 1
    else:
        print("YOU MADE THE RIGHT GUESS",end=" ")
        print(f"THE ANSWER IS {answer}")

def Game():
    print(logo)
    print("Welcome to the Number Guessing GAME ")
    turns = difficulty()
    print("Thinking of a number between 1 and 100 !")
    answer = random.randint(1,100)
    guess = 0 
    while guess !=answer:
        print(f"You have {turns} turns remaining until the end of the game")  
        guess = int(input("Enter the Guessed Number:")) 
        turns = check(guess,answer,turns)
        if turns == 0:
            print("GAME OVER")
            return
        else:
            print("Guess Again!")     
Game()
