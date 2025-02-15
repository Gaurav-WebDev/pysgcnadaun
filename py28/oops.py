# class MyClass:

#     def __init__(self , name , rollNo):
#         self.stdName = name
#         self.stdRollNo = rollNo
    
#     def showInfo(self):
#         print(f"Student Name : {self.stdName} , Roll No : {self.stdRollNo}")

# std1 = MyClass("Raj" , 101)
# std2 = MyClass("Rohit" , 102)

# std2.showInfo()


# ===>

class Parent:
    def fun1(self):
        print("Hello i am parent")

class Child(Parent):
    def fun2(self):
        print("Hello i am Child")

# p1 = Parent()
# p1.fun1()
# p1.fun2()

c1 = Child()
c1.fun1()
c1.fun2()

