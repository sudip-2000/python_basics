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





"""........................................................access tuple..................................................."""

#print the third item of tuple

student_tuple =("ram", "shyam", "krishna", "hari", "hari", "ram",)
print("3rd item of this  tuple: ", student_tuple[2])


"""..........................................................................................................................."""



#negative indexing (start from the last)

#print the last item of tuple

student_tuple =("ram", "shyam", "krishna", "hari", "hari", "ram", "gita")
print("last item of tuple: ", student_tuple[-1])


"""..........................................................................................................................."""




#print the 2nd, 3rd, 4th and 5th item from tuple

student_tuple =("ram", "shyam", "krishna", "hari", "hari", "ram","gita")
print("2nd to 5th items in tuple: ", student_tuple[1:5])
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included


"""..........................................................................................................................."""


"""........................................................................................................................................"""



#check if krishna is present in the tuple

student_tuple =("ram", "shyam", "krishna", "hari", "hari", "ram", "gita")
if "krishna" in student_tuple:
    print("yes, krishna is present in the tuple")



"""..........................................................................................................................."""







