""".............................................dictionary related question.........................................."""

#Create a dictionary where keys are numbers from 1 to 5, and values are their squares.

dict_1=dict( ((x,x**2) for x in range(1,6)))
print("dictionary: ",dict_1)

"""..............................................................................."""


#Write a program to merge two dictionaries.


dict_1={"type":"car", "brand":"honda", "electric":"False"}
dict_2={"year":2024, "colors":["red", "blue", "green"]}

dict_1.update(dict_2)
print("merged dictionary: ",dict_1)


"""................................................................................"""


#Count the frequency of each character in a string using a dictionary.


string_name="the quick and brown fox jumps over the lazy dog"
this_dict=dict()

for i in string_name:
    if i in this_dict:
        this_dict[i]+=1
    else:
        this_dict[i]=1

print("the frequency of each character: ",this_dict)


""".................................................................................."""


#Sort a dictionary by its keys.

dict_1={"type":"car", "brand":"honda", "electric":"False"}
dict_1=sorted(dict_1.keys())
print("sorted dictionary: ",dict_1)

""".................................................................................."""



#Write a program to find the maximum and minimum value in a dictionary.

dict_1=dict( ((x,x**2) for x in range(1,6)))
print("maximum value: ",max(dict_1.values()))
print("minimum value: ",min(dict_1.values()))


"""................................................................................"""




