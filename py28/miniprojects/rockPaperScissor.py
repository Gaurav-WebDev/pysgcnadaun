import random 

options = ["Rock" , "Paper" , "Scissor"]
computerChoice = random.choice(options)

userChoice = "Rock"

choice = int(input("Enter your choice ( Default : Rock ) \n1 for Rock \n2 for Paper \n3 for Scisssor:"))

if choice == 1:
    userChoice = "Rock"
elif choice == 2:
    userChoice = "Paper"
elif choice == 3:
    userChoice = "Scissor"
else:
    pass

print(f"Computer Choice : {computerChoice} ")
print(f"User Choice : {userChoice} ")

