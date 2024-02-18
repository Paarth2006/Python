from art1 import logo, vs
from game_data import data
import random
def random_account():
    return random.choice(data)

def fdata(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"
    
def check(guess,afollowers,bfollowers):
    if afollowers>bfollowers:
        return guess == "a"
    else:
        return guess == "b"
    
def game():
    print(logo)
    score = 0
    continue_game=True
    accounta = random_account()
    accountb = random_account()
    
    while continue_game:
        accounta = accountb
        accountb = random_account()
        while accounta == accountb:
            accountb = random_account()
        print(f"Compare A:{fdata(accounta)}")
        print("VS")
        print(f"With B:{fdata(accountb)}")
        guess = input("Who Has More followers ? Type A or B :").lower()
        afollowerscount = accounta["follower_count"]
        bfollowerscount = accountb["follower_count"]
        correct = check(guess,afollowerscount,bfollowerscount)
        print(logo)
        if correct:
            score += 1
            print(f"You are Right! Current Score:{score}")
        else:
            continue_game = False
            print(f"Sorry! Thats the End, Final Score:{score}")
game()
