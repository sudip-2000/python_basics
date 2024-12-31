#Write a program to check the type of the variables

int_num=10
float_num=0.0009
name="sudip"
boolean_type=True
complex_num=7j

print(type(int_num))
print(type(float_num))
print(type(name))
print(type(boolean_type))
print(type(complex_num))




#Convert a float value 45.67 to an integer and print the result.

x=45.67
print("value of x:",x)
print("datatype of x:",type(x))

x=int(x)
print("int x:",x)





#Create a list of five integers, access the third element, and change its value.

numbers=[1,2,3,4,5]
print("List of numbers before change:",numbers)

numbers[2]=9
print("List of numbers after change:",numbers)



#Create a dictionary with three key-value pairs representing a student’s name, age, and grade. Access the age value.

student={
    "name":"ram",
    "age":20,
    "grade":"10th"
}

print("student age:",student["age"])




