from capitals import states

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

    for state in states:
        guess_capital = input("What is the capital of " + state["name"] + "?")

        if guess_capital == state["capital"]:
            print("Look at you, all smart and stuff!")
            correct_count += 1
        else:
            print("Yeah...Not quite right.")
            incorrect_count += 1

        print("Correct: {}".format(correct_count))
        print("Incorrect: {}".format(incorrect_count))

begin()