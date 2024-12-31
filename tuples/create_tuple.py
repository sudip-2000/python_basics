""" 
Tuples are used to store multiple items in a single variable   
A tuple is a collection which is ordered and unchangeable
Tuples are written with round brackets ()
 
"""


"""..........................................................................................................................."""

#create a tuple

this_tupple=("ram", "shyam", "krishna", "hari")
print(this_tupple)


"""..........................................................................................................................."""




#tuple allows duplicate values

student_tuple =("ram", "shyam", "krishna", "hari", "hari", "ram",)
print(student_tuple)


"""..........................................................................................................................."""




#print number of items in tuple

student_tuple =("ram", "shyam", "krishna", "hari", "hari", "ram",)
print("total number of items in tuple: ", len(student_tuple))


"""..........................................................................................................................."""




#one item tuple

#one item tuple, remember the comma.
one_item_tuple =("apple",)
print(one_item_tuple)
print(type(one_item_tuple))

#NOT a tuple , without comma its just a string 
one_item_tuple=("apple")
print(one_item_tuple)
print(type(one_item_tuple))


"""..........................................................................................................................."""





#tuple items can be any data types

tuple_1 =("ram", "shyam", "krishna", "hari", "hari", "ram",)
tuple_2=(1, 2, 3, 4, 5)
tuple_3=(True, False, True, False )
print(tuple_1, tuple_2, tuple_3)


"""..........................................................................................................................."""




#tuple with different data types like string, integer, boolean values

different_datatypes_tuple =("ram", 1, True, "male", 20)
print("different data types tuple: " , different_datatypes_tuple)


"""..........................................................................................................................."""












