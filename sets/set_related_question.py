"""......................................set related question................................................"""

#Find the common elements between two sets.

set_1={1,2,3,4,5}
set_2={4,5,6,7,8}

set_3= set_1 & set_2
print("using & operator: ",set_3)


#we can also use intersection() method instead of & operator   and get the same result

set_3= set_1.intersection(set_2)
print("using intersection() method: ",set_3)


"""................................................................................................................."""


#Write a program to remove all duplicates from a list using a set.

my_list=[1,2,3,4,5,6,7,8,0,1,2,3,4,5,6,7,8,9,10]
my_set= set(my_list)
print(my_set)



""".................................................................................................................."""


#Check if a set is a subset of another set.

set_1={1,2,3,4,5}
set_2={4,5,6,7,8}

print(set_2.issubset(set_1))

""".................................................................................................................."""


#Write a program to find the symmetric difference between two sets.

set_1={1,2,3,4,5}
set_2={4,5,6,7,8}

set_3= set_1^set_2
print("using ^ operator: ",set_3)


#we can also use symmetric_difference() method instead of ^ operator   and get the same result

set_3= set_1.symmetric_difference(set_2)
print("using symmetric_difference() method: ",set_3)




"""................................................................................................................."""



#Create a set of unique characters from a string.


name="hippopotamus"
set_1= set(name)
print("set of unique characters: ",set_1)



