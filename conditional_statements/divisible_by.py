"""WAP that takes an integer and determines whether it is divisible by 2,3 or both using a combination of logical operators and conditions."""

num=int(input("enter number: "))


if num%3==0 and num%2==0:
    print("it is divisible by both 2 and 3")
    
elif num%3==0:
        print("it is divisible by 3")
        
elif num%2==0:
    print("it is divisible by 2")
    
else:
    print("it is neither divisible by 2 nor 3")

