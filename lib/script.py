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
    print("This is where the game goes!")

begin()