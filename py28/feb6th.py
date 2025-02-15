# ==> and | or | not ( logical oper)

# a = 8

# print(a < 5 and a < 20)
# print(a < 5 or a < 20)
# print(not (a < 5 or a < 20))

# ==> f string

# name = "Raj"
# age = 34

# print("Hello" , name , "and age is" , age)
# print(f"Hello {name} and age is {age}")

# ==> while loop

# age = 21

# while age <= 18:
#     print(f"Age : {age}")
#     age += 1


# ============

# marks = int(input("Enter your marks(1 to 100) : "))

# while marks < 1 or marks > 100:
#     print("Please enter your correct marks")
#     marks = int(input("Enter your marks(1 to 100) : "))


# ==========

# for i in range(1 , 11):
#     print(i)
#     if i == 5:
#         break
  
# for i in range(1 , 11):
#     if i == 5:
#         continue

#     if i == 7:
#         continue

#     print(i)


# ====> functions in python

# def sayHello(name):
#     print(f"Hello welcome {name}")

# sayHello("Raj")
# sayHello("Rajat")
# sayHello("Rohit")

# =====

def add(a , b):
    print(f"{a} + {b} = {a + b}")
    return a + b


sum = add(10 , 20)
# add(12 ,21)
# add(345 , 789)
print(sum)
  