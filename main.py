import random

randNo = random.randint(1,50)

userGuess = None
guesses =0

print("Guess any Number from 1 - 50 ")
while(userGuess != randNo):
    userGuess = int(input("Enter your guess: \n"))
    guesses+=1
    if(userGuess == randNo):
        print("Great!! You guessed it right!")
    else:
        if(userGuess>randNo):
            print("Oops! You guessed it Wrong!")
            print("Enter a smaller number")
        else:
            print("Oops! You guessed it Wrong!")
            print("Enter a larger number")


print(f"You guessed the number in {guesses} guesses")
with open("highest_score.txt","r") as f:
    highest_score = int(f.read())
if(guesses<highest_score):
    print("you have just broken the high score!!")
    with open("highest_score.txt","w") as f:
        f.write(str(guesses))
        