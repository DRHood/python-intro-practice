from capitals import states
from responses import correct
from responses import incorrect
import random

print("How well do you know your state capitals?")
print("Let's find out.")

def begin():
    begin = input("Would you like to play a game? (y/n)")
    if begin == "y":
        return play_game()
    else:
        print("Maybe next time.")
        return

def play_game():
    correct_count = 0
    incorrect_count = 0

    random.shuffle(states)

    for state in states:
        guess_capital = input("What is the capital of " + state["name"] + "?")

        if guess_capital == state["capital"]:
            print(random.choice(correct))
            correct_count += 1
        else:
            print(random.choice(incorrect))
            incorrect_count += 1

        print("Correct: {}".format(correct_count))
        print("Incorrect: {}".format(incorrect_count))

    play_again = input("Would you like to play again? (y/n)")
    if play_again == "y":
        return play_game()
    else:
        print("Until next time...")
        return

begin()