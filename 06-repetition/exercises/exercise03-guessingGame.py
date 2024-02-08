import random

correct_number = random.randint(1, 10)

guess = int(input("Guess a number 1 - 10 : "))
while guess != correct_number:
    guess = int(input("Guess a number 1 - 10 : "))

print("You're correct!")

