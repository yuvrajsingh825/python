#Number Guessing 
import random
number = random.randint(1,100)
guess = None

while guess !=number:
    guess = int(input("Guess the number between 1 and 100: "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
else:
    print("Congratulations! You guessed the number.")
#only 5 chances to guess the number 
 

guess_count = 5
while guess_count > 0:
    guess = int(input("Guess the number between 1 and 100: "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        break
    guess_count -=1
if guess_count == 0:
    print("Sorry, you've used all your chances. The number was:", number)


