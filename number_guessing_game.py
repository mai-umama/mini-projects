import random 

target = random.randint(1,100) #range
while True :
    userChoice = (input("Guess the target need to be a valid number or Quit: "))

    if(userChoice == "Quit"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success: Correct guess!!")
        break
    elif(userChoice > target):
        print("Sorry number is too big. Take a smaller number..")
    else:
        print("Sorry number is too small. Take a bigger number..")   

print("------Game Over------")    