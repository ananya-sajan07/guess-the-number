import random
compChoice = random.randint(1, 100) 
userChoice = -1
guesses = 1
while(userChoice != compChoice):
    userChoice = int(input("Guess the number: ")) 
    if(userChoice > compChoice):
        print("Lower number please")
        guesses +=1
    elif(userChoice < compChoice):
        print("Higher number Please")
        guesses +=1

print(f"You have guessed the number {compChoice} correctly in {guesses} attempts")