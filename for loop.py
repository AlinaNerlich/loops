import random

secret = random.randint(1, 100)

for x in range(10):
    user_input = input("Guess a number between 1 and 100: ")
    guess = int(user_input)

    if guess == secret:
        print("OK")
        break
    elif guess < secret:
        print("too small")
    else:
        print("too big")