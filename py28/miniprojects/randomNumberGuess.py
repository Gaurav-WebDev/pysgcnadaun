import random 
randomNum = random.randint(1 , 100)
# print(randomNum)
while True:
    userNum = int(input("Guess a number from 1 to 100:"))
    if userNum < 1 or userNum > 100:
        print("Please enter correct value")
    elif userNum > randomNum:
        print("Your guess is too high")
    elif userNum < randomNum:
        print("Your guess is too low")
    elif userNum == randomNum:
        print("Right Guess")
        break
    else:
        print("Something went wrong")