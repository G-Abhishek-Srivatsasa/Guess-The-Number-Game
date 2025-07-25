import random
x = random.randint(1,15)

hint1 = "The number is EVEN" if x % 2 == 0 else "The number is ODD"
hint2 = "The number is > 8" if x > 8 else "The number is < 8"
hint3 = "The number is a multiple of 3" if x % 3 == 0 else "The number is not a multiple of 3"
score = 0
X = [hint1, hint2, hint3]
Y = [hint1, hint2, hint3]

X = random.choice(X)
Y = random.choice(Y)


print("   Welcome to the Guess The Number Game!")
print('   The Rules of the Game are simple:')
print("1. I will randomly select a number between 1 and 15.")
print("2. There will be 3 Guesses for you !")
print("3. You will type hint when ever you want..." )
print("   PRESS ENTER TO START THE GAME!")
                                                                         # for GUESS 1
if int(input("Enter a number between 1 and 15: ")) == x:
    print("CONGRATS! , You got a point!")
    score += 1
    print("YOUR SCORE :" , score)
    print("YOU WON THE GAME!!!!!!")
else:
    print("Sorry! , You guessed it wrong , try again!!")
    if input("HINT / CONTINUE :") == "hint":
        print(X)
    elif input("Press Enter to confirm") == "":
        print("Fine , No hint!!")
    if int(input("Enter a number between 1 and 15: ")) == x:              # for guess 2
        print("CONGRATS! , You got a point!")
        score += 1
        print("YOUR SCORE :" , score)
        print("YOU WON THE GAME!!!!!!")
    else:
        print("Sorry! , you got it wrong , try again!!")
        if input("HINT / CONTINUE :") == "hint":
            print(Y)
        else:
            print("Fine , No hint!!")
    if int(input("Enter a number between 1 and 15: ")) == x:              # for guess 3
              print("CONGRATS! , You got a point!")
              score += 1
              print("YOUR SCORE :" , score)
              print("YOU WON THE GAME!!!!!!")
    else:
             print("Sorry! , you got it wrong , NO MORE CHANCES LEFT!!")
    print(x)
             
  
    
   

















