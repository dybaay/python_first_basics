import random

def play(num, random_number):
    res = ""
    if num > random_number:
        res = "Too high"
    if num < random_number:
        res = "Too low"
    if num == random_number:
        res = "Congratulations you got it right"
    return res

attempts = 0
random_number = random.randint(1, 10)

while True:
    if attempts == 3:
        print("Attemps exceeded")
        break
    attempts +=1
    guess_number = float(input("Guess the number: "))
    print(play(guess_number, random_number))
    if play(guess_number, random_number) == "Congratulations you got it right":
        break
   