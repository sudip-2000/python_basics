"""you can use both remove() or discard() method to remove items from set
remove() will raise an error if item to remove does not exist
discard()  will not raise any error if item to remove does not exist

"""

""".............................................................................."""

#remove item using remove() method

set_1={1,2,3,4,5,6,7,8}
print("before removing item: ", set_1)

set_1.remove(5)
print("after removing item: ", set_1)


"""................................................................................"""



#remove item using discard() method

set_2={"ram", "shyam", "sita"}
print("before discarding item: ", set_2)

set_2.discard("shyam")
print("after discarding item: ",set_2)



"""...................................................................................."""


#we can also use pop() method to remove item from set but we do not know which item gets removed

set_3={"apple", "banana", "mango", "grape", "pineapple"}
x=set_3.pop()

print(x)
print(set_3)


"""............................................................................................."""


#the clear() method empties the set

set_4={1,2,3,4,5}
set_4.clear()

print(set_4)




"""...................................................................................................."""



# del keyword will delete set completely

set_5={1,2,3,4,5,6,7,8}
del set_5

print(set_5)


