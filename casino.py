import random
import json
import datetime

secret = random.randint(1,10)
attempts = 0

player = input("Hello, What is your name? ")

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())

for score_dict in score_list:
    print (str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))

while True:
    guess = int(input("Guess the secret number: (between 1 and 10): "))
    attempts += 1

    if secret == guess:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})

        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("Congratulations, you won $1,000 !!!")
        print("Attempts needed: " +str(attempts))
        break
    elif guess < secret:
        print("Your guess is too small.")
    elif guess > secret:
        print("Your guess is too big.")


