import random
import json
import datetime
import operator

secret = random.randint(1,10)
attempts = 0
wrong_guesses = []

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())

score_list.sort(key=operator.itemgetter("attempts"))

for score_dict in score_list[:3]:
    score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}"\
                 .format(score_dict.get("player_name"),
                        str(score_dict.get("attempts")),
                        score_dict.get("date"),
                        score_dict.get("secret_number"),
                        score_dict.get("wrong_guesses"))
    print(score_text)


player = input("Enter player name: ")

while True:
    guess = int(input("Guess the secret number: (between 1 and 10): "))
    attempts += 1

    if secret == guess:
        score_list.append({"attempts": attempts, "wrong guesses": wrong_guesses, "secret_number": secret,
                           "player": player, "date": str(datetime.datetime.now())})

        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("Congratulations, you won $1,000 !!!")
        print("Attempts needed: " + str(attempts))
        break
    elif guess < secret:
        print("Your guess is too small.")
    elif guess > secret:
        print("Your guess is too big.")

    wrong_guesses.append(guess)
