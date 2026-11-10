import random


secret = random.randint(1, 20)
guess = 0
count = 0

print("I'm thinking of a number between 1 and 20.")

while guess != secret:
    guess = int(input("Your guess: "))
    count = count + 1
    if guess < secret:
        print("Higher!")
    elif guess > secret:
        print("Lower!")
print("You got it in", count, "tries!")