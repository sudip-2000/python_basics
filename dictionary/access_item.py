"""...............................Access Items in a Dictionary............................"""


#access the value of the "name" key

my_dict = {
    "name": "Ram",
    "age": 25,
    "address": "kathmandu"
}
print(my_dict["name"])



#there is also get() method to access the value of a key

print(my_dict.get("name"))



""".......................key () method.............................................."""


#the key() method returns a list of all the keys in the dictionary

thisdict = {
    "brand": "Ford",
    "color": "red", 
    "year": 1914
}


print(thisdict.keys())


"""..........................................................................................."""