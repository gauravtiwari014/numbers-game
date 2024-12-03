import random
target=random.randint(1,100)
while True:
    userChoice=input("Guess the target or quit:")
    if(userChoice=="Quit"):
        break
    userChoice= int(userChoice)
    if(userChoice==target):
        print("Success:Correct Guess!!")
        break
    elif(userChoice<target):
        print("your number was too small.Take a bigger guess...")
    else:
        print("your number was too big.Take a smaller guess...")
        print("_ _ _ _ _ GAME OVER _ _ _ _ _")
