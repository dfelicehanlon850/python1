#creating the coin flip game

import random
print("WELCOME TO THE COIN FLIP GAME")
print("Guess heads by entering 1 or tails by entering 0.");
guess = int(input())
if(guess == 1):
    print("You guessed heads.")
else:
    print("you guessed tails.")
flip = random.choice([1,0])
if(guess == flip):
    print("Congrats You WIN")
else:
    print("Sorry You LOSE.")
