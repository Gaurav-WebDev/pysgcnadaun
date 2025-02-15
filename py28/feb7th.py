# def add(a , b):
#     return a+b


# print(add(10 , 20))  #==> callback function


# ===> Default Arguments

# def add(a=0 , b=0):
#     return a+b

# print(add(10 , 34))

# ====> keyword arguments

# def showInfo(name , age):
#     print(f"Hello {name} and age {age}")

# showInfo(age=45 , name="Mohit")

# =====>

# def data(**all):
#     print(all)

# data(a = 10 , b = 20 , c = 30)

# ===> Variable Scope

# a = 10
# b = 0
# def add():
#     b = 5
#     print(a + b)

# print(a + b)
# add()
# print(a + b)


# ======>


# for i in range(1 , 11):
#     print(i)

# data = (10 , 20 ,33 ,44 ,55 ,66)

# for i in data:
#     print(i)


# def add(*all):
#     sum = 0
#     for i in all:
#         sum = sum + i
#     print(f"Sum : {sum}")

# add(10 , 20 , 30 , 40 , 5)

# ===>  

def findFact(num):
    if num == 1:
        return 1
    else :
        return num * findFact(num - 1)

print(findFact(4))