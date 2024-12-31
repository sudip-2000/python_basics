"""sets are used to store multiple items ina a single variable."""
"""A set is a collection which is unordered, unchangeable*, and unindexed"""
"""sets are written with curly brackets {}"""

""".............................................................................................."""


#create a set
thisset={"apple", "banana", "mango"}
print(thisset)



"""................................................................................................"""

#duplicate is not allowed in set

set_1={1,2,3,4,2,1} # here the duplicate values will be ignored
print(set_1)



"""...................................................................................................."""

#the values like True and 1 , False and 0 are considered as same in sets, and treated as duplicates

set_2={True,1,False, 0}
print(set_2)
print(type(set_2))


"""....................................................................................................."""



#find the number of items in sets {1,2,3,4,5,6,7,90,87,43,12,78}

set_3={1,2,3,4,5,6,7,90,87,43,12,78}
print("the number of items in this set is: " ,len(set_3))



"""......................................................................................................."""



#create a sets with different data types

set1={"ram", "shyam"}
set2={1,2,3,4,5,6,7}
set3={True, False}

print(set1)
print(set2)
print(set3)




"""......................................................................................................................"""




