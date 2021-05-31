import random
# --> random number guess game with storing high score every time you break high score

randNo = random.randint(0, 100)
userGuess = None
guesses = 0
while userGuess != randNo:
    userGuess = int(input("Enter your number: \n"))
    guesses += 1
    if userGuess == randNo:
        print("Yes, You guessed right!!")
    elif userGuess > randNo:
        print("you guessed it wrong, Guess something small")
    else:
        print('you guessed it wrong, Guess something big')

print(f"all the guesses are {guesses}")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if (guesses < hiscore):
    print("hurray you just broke the high score!!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
