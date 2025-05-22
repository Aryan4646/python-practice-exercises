 # a number guessing game where the user tries to guess a random number in limited attempts.
import random

random_num = random.randint(1,10)
print("Welcome to number guess game!")
lives = 5

while lives > 0:
    num = int(input("Enter the guess number between 1 to 10: "))
    if num == random_num:
        print("You chose the correct number. You won")
        break
    else:
        lives -= 1
        print(f"You chose wrong number.Lives remaining are: {lives}")
else:
    print("You lost Loser")
