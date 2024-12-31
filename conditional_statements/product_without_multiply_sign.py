"""without using * , write a program to calculate the product of two integers"""

num_1= int(input("enter first number: "))
num_2= int(input("enter second number: "))  

sum=0
for i in range(1, num_2+1):
    sum=sum+num_1

print(sum)


