#import dependencies
import random

# select a random number from 1 to 20
number = random.randint(1,20)

print("I am thinking of a number between 1 and 20...\n")
print("Try to guess the number in less than 6 tries!")
 
# give user 6 tries to guess the number.
# if they guess correctly, they win!
# if they do not, they lose, and the game is over. 
for i in range(7):
    if i > 0:
        guess = int(input("What number am I thinking of? "))
        if guess == number:
            print("Wow! You guessed correctly!!")
            break
        if i == 6:
            print("You ran out of tries. Better luck next time. \n")
        else:
            print(f"Sorry. You didn't guess the number. You have {6-i} tries left. \n")