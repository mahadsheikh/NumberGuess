import random

top_range = input("Type a Number : ")

if top_range.isdigit():
    top_range = int(top_range)
    if top_range < 0 :
        print("Please type a number greater than 0")
else:
    print("Please type a number ")

random_number = random.randint(0,top_range)
print(random_number)