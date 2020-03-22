from capitals import states
from responses import correct
from responses import incorrect
import random

print("\n")
print("How well do you know your state capitals?")
print("Let's find out.")
print("\n")

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
        print("\n For a 3 letter hint, enter (H)")
        guess_capital = input("What is the capital of " + state["name"] + "?")

        if guess_capital == "H":
            print(state['capital'][:3])
            print("")
            while (guess_capital == "H"):
               guess_capital = input("What is the capital of " + state["name"] + "?")
            if guess_capital == state["capital"]:
                print("\n" + random.choice(correct))
                correct_count += 1
            else:
                print("\n" + random.choice(incorrect))
                print(state["capital"])
                print("")
                incorrect_count += 1
        elif guess_capital == state["capital"]:
            print("\n" + random.choice(correct))
            correct_count += 1
        else:
            print("\n" + random.choice(incorrect))
            print(state["capital"])
            print("")
            incorrect_count += 1

        print("You've answered {}".format(correct_count) + " out of {}".format(correct_count + incorrect_count) + " correctly.")
        print("Correct: {}".format(correct_count))
        print("Incorrect: {}".format(incorrect_count))

    play_again = input("\n Would you like to play again? (y/n)")
    if play_again == "y":
        return play_game()
    else:
        print("Until next time...")
        return

begin()