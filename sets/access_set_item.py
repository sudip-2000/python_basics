"""
you can not access items in a set by referring to an index or a key
But you can loop through set using for loop, or ask for a specific value is present ina aset, by using in keyword

"""


""".............................................................."""



#loop through the set, and print the values
set_1= {"ram", "shyam", "hari"}

for x in set_1:
    print(x)
    
    

"""...................................................................."""




#check if any specific item is present in the set

set_2={"apple", "banana", "mango", "pineapple"}
print("pineapple" in set_2)
print("watermelon" in set_2)
print("apple" not in set_2)
print("watermelon" not in set_2)

