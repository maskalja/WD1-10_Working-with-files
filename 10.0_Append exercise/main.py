
import random
secret = random.randint(1, 30)
attempts = 0

with open("highscores.txt", "r") as highscores_file:
    highscore = highscores_file.readlines()[-1]
    print("Current best score is {0} guesses. Can you beat it?".format(highscore))

while True:
    guess = int(input("Guess the number: "))
    attempts += 1
    if guess == secret:
        print("You have guessed the number in just {0} attempts.".format(attempts))
        if attempts < int(highscore):
            with open("highscores.txt", "a") as highscores_file:
                highscores_file.write("\n")
                highscores_file.write(str(attempts))
            print("Congrats, you set new highscore ({0} attempt/-s). You're a h4Ck3R for sure!".format(attempts))
        break
    elif guess < secret:
        print("Try with a HIGHER number.")
    elif guess > secret:
        print("Try with a LOWER number.")