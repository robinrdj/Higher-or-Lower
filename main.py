# importing logo
from art import logo
from replit import clear
from art import vs
from game_data import data
import random


# functions
def format_data(account):
    """ takes the account data and return the printable format """
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description} from {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# generating a random account from the game data
account_b = random.choice(data)
should_continue = True
print(logo)
while should_continue:
    account_a = account_b
    account_b = random.choice(data)
    print(f"compare {format_data(account_a)}")
    print(vs)
    print(f"compare {format_data(account_b)}")

    # asking user for a guess
    guess = input("make a guess. who has more followers. 'A' or 'B'\n").lower()

    # get follower count for each account
    # check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # give users feedback on their guess
    # keeping the scores
    score = 0
    print(is_correct)
    if is_correct:
        print("U r right")
        score += 1
    else:
        should_continue = False
        print("U r wrong")
        print(f"ur score is {score}")

