import random

top_range = input("Type a Number : ")
if top_range.isdigit():
    top_range = int(top_range)
    if top_range < 0 :
        print("Please type a number greater than 0")
else:
    print("Please type a number ")

random_number = random.randint(0,top_range)
guesses = 0
while True:
    guesses += 1
    usr_guess = input("make a guess : ")
    if usr_guess.isdigit():
        usr_guess = int(usr_guess)
    else:
        print("Please type a number ")
        continue

    if usr_guess == random_number:
        print("You guessed it")
        break
    else:
        print("You guessed incorrect")

print("you got it in ",guesses," guesses")