"""....................................Dictionary.........................................."""


"""
dictionaries are used to store data values in key:value pairs
a dictionary is a collection which is ordered*, changeable and does not allow duplicates
dictionaries are written with curly brackets {} and have keys and values

"""



"""............................................create a dictionary..................................................."""

# create a dictionary and print it
my_dict = {
    "name": "Ram",
    "age": 25,
    "address": "kathmandu"
}
print(my_dict)
print(type(my_dict))






"""............................................print the address value from the dictionary..................................................."""




my_dict = {
    "name": "Ram",
    "age": 25,
    "address": "kathmandu"
}

print(my_dict["address"])




"""............................................duplicate values in dictionary..................................................."""

#duplicate values are not allowed in dictionary
#duplicate values will overwrite existing value

my_dict = {
    "name": "Ram",
    "age": 25,
    "address": "kathmandu",
    "address": "Lalitpur"
}
print(my_dict)



"""............................................dictionary length..................................................."""

#to determine how many items a dictionary has, use the len() function


my_dict = {
    "name": "Ram",
    "age": 25,
    "address": "kathmandu"
    }
print(len(my_dict))


"""............................................dictionary items..................................................."""

#the values in dictionary items can be of any data type

dict_1 = {
    "type": "car",
    "brand": "honda",
    "electric": False,
    "year": 2024,
    "colors": ["red", "blue", "green"]
}
print(dict_1.items())



"""............................................dict() constructor..................................................."""
#use the dict() constructor to create a dictionary


dict_2 = dict(name="Ram", age=25, address="kathmandu")
print(dict_2)


