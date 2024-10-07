# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.


import random


def game():
    print("Playing game...")
    score = random.randint(1, 62)
    # fetch the hi-score from the file
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score: {score}")
    if score > hiscore:
        # write the new hiscore to the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
            print("New hi-score is set")

    return score


game()
