"""there are different ways to join two sets in python
like union(), update(), intersection(), difference(), symmetric_difference()"""


"""................................................................................................"""

#union() method returns a new set with all items from both sets.


# we can also use | operator instead of union() and get the same result


set_1={1,2,3,4}
set_2={"a", "b"}

set_3= set_1.union(set_2)
print(set_3)




"""...................................................................................................."""





#join multiple sets using union() method

num_set= {1,2,3,4,5,6,7,8}
name_set= {"ram", "shyam"}
boolean_set={True, False}
fruit_set= {"apple", "banana", "grapes"}

my_set= num_set.union(name_set, boolean_set, fruit_set)
print ("joined multiple set: ", my_set)


"""............................................................................................................"""


#join multiple sets using | operator instead of union() method

num_set= {1,2,3,4,5,6,7,8}
name_set= {"ram", "shyam"}
boolean_set={True, False}
fruit_set= {"apple", "banana", "grapes"}

my_set= num_set | name_set| boolean_set | fruit_set 
print ("joined multiple set using | operator: ", my_set)


"""..............................................................................................................."""


# join a set with a list using union() method

student_set={"ram", "shyam", "sita"}
student_list=["gita", "rita"]

union_set= student_set.union(student_list)
print("joined set: ", union_set)


""".................................................................................................................."""




# join two sets using intersection()
# it only keeps duplicates

set_a={1,2,3,4,5}
set_b={3,4,5,6,7,8,9}

set_c= set_a.intersection(set_b)
print(set_c)


#we can also use & operator instead of intersection() METHOD and get the same result



"""...................................................................................."""



# intersection_update()
# this method will also keep only the duplicates, but it will change the original set


fruit_set_1={"apple", "banana", "grapes"}
fruit_set_2={"apple", "banana", "mango", "pineapple"}

fruit_set_1.intersection_update(fruit_set_2)

print(fruit_set_1)



"""....................................................................................................."""




# difference method
#this method will return a new set that will contain only the items from the first set that are not present in the other set


first_set={"apple", "banana", "cherry"}
second_set={"apple", "microsoft", "google"}

third_set= first_set.difference(second_set)

print(third_set)

# we can use - operator instead of difference() method and get the same result



""".............................................................................................................................."""



#difference_update()
# this method updates the current set instead of returning new set
#it keeps the items that are not present in both sets


set_first={"apple", "banana"}
set_second={"google", "apple", "microsoft"}

set_first.difference_update(set_second)

print(set_first)




"""............................................................................................"""


#symmetric_difference()
#this method only keeps the elements that ate not present in both sets


set_first={"apple", "banana"}
set_second={"google", "apple", "microsoft"}

set_third=set_first.symmetric_difference(set_second)

print(set_third)

#we can also use ^ operator instead of summetric_difference() method



"""............................................................"""




#symmetric_difference_update()
#this updates the existing set


set_first={"apple", "banana"}
set_second={"google", "apple", "microsoft"}

set_first.symmetric_difference_update(set_second)

print(set_first)




