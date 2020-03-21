from capitals import states

print("How well do you know your state capitals?")
print("Let's find out.")

for state in states:
    state["correct"] = 0
    state["incorrect"] = 0

def begin():
    begin = input("Would you like to play a game? (y/n)")
    if begin == "y":
        return play_game()
    else:
        print("Maybe next time.")
        return

def play_game():
    for state in states:
        guess_capital = input("What is yhe capital of " + state["name"] + "?")

        if guess_capital == state["capital"]:
            print("Look at you, all smart and stuff!")
            state["correct"] += 1
        else:
            print("Yeah...Not quite right.")
            state["incorrect"] -= 1
        print("Correct: {}".format(state["correct"]))
        print("Incorrect: {}".format(state["correct"]))

begin()