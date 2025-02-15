# list1 = [12, 34 ,56 ,78 ,90 , 47 , 8 , 77 , 99 , 41 , 66]

# # filterList = list(filter(lambda x : (x%2==0) , list1))
# # filterList = list(filter(lambda x : (x>40) , list1))

# mapList = list(map(lambda x : x+5 , list1))

# print(list1)
# # print(filterList)
# print(mapList)



# ========>

# try:
#     num1 = int(input("Enter your 1st number: "))
#     num2 = int(input("Enter your 2nd number: "))
#     print(f"{num1} + {num2} = {num1 + num2}")
# except :
#     print("num1 and num2 must be a number")

# print(10/0)


# ==>

try : 
    num1 = int(input("Enter your 1st number: "))
    num2 = int(input("Enter your 2nd number: "))
    print(f"{num1} / {num2} = {num1 / num2}")
except ValueError:
    print("ERROR : num1 and num2 must be a number")
except ZeroDivisionError:
    print("infinity")