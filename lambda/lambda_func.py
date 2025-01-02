"""
lambda function is a small anonymous function
it is used to create a function without a name
lambda function can take any number of arguments but can have only one expression

"""
"""....................................................................................."""


#add 20 to argument a and return the result

add_20=lambda a:a+20
print(add_20(10))


"""....................................................................................."""


#multiply argument a with argument b and return the result

multiply=lambda a,b:a*b
print(multiply(10,20))



"""....................................................................................."""



#summarize argument a,b,c and return the result

summarize=lambda a,b,c:a+b+c
print(summarize(10,20,30))




"""....................................................................................."""


#write a lambda function to find the maximum of two numbers?

max_num=lambda a,b: a if a>b else b
print(max_num(100,200))



"""....................................................................................."""


#Write a function that uses a lambda function to add a fixed number to any given number.

def add_fixed_number(fixed):
    return lambda x: x+fixed

add_10= add_fixed_number(10)

print(add_10(5))




"""....................................................................................."""



#Write a function that returns a lambda function to calculate the power of a number.

def power(n):
    return lambda x: x**n

square= power(2)
print(square(3))

square= power(3)
print(square(3))



"""....................................................................................."""





