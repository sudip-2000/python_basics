

class A:
    def display(self):
        print("class A method")

class B:
    def display(self):
        print("class B method")

class Demo(A,B):
    def show(self):
        print("class demo method")
    
print(Demo.__mro__)  
# print(Demo.mro())
# demo=Demo()
# demo.display()


