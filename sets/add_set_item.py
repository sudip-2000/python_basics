"""you cannot change items of set once its created
But you can add new items in set 
"""

""".........................................................................."""

# add an item to a set

add_item={1,2,3,5,67,7}
print("set before adding new item: " ,add_item )

add_item.add(100)
print("set after adding new item: ", add_item)


""".............................................................................."""



# add items of another set into current set

current_set={"1,2,3,4,5,6"}
previous_set={"rem", "shyam", "hari"}

current_set.update(previous_set)
print(current_set)



"""...................................................................................."""


#using update() method we can add not just a set but any iterable object(tuples, lists, dictionaries etc.)

my_set={"apple", "banana"}
my_tupple=(1,2,3,4)
my_list=[00,000,111,222,333]

my_set.update(my_tupple)
print(my_set)

my_set.update(my_list)
print(my_set)




