""".......................................tuple related question..........................................."""



#Write a program to swap the first and last elements of a tuple.

my_tuple=("ram", "shyam", "krishna", "hari", "hari", "ram", "gita")
print("tuple before: ", my_tuple)

my_list=list(my_tuple)

my_list[0], my_list[-1]= my_list[-1], my_list[0]


my_tuple=tuple(my_list)
print("tuple after: ", my_tuple)



"""..........................................................................................................................."""


#Unpack the tuple `(10, 20, 30, 40)` into four variables and print them.

tuple_1=(10, 20, 30, 40)
a,b,c,d= tuple_1

print("a: ", a)
print("b: ", b)     
print("c: ", c)
print("d: ", d)




"""..........................................................................................................................."""




#Convert a list into a tuple and vice versa.


thislist = ["apple", "banana", "cherry"]
thistuple = tuple(thislist)

print("this is tuple: ",thistuple)


thislist = list(thistuple)
print("this is list: ",thislist)


"""..........................................................................................................................."""



#Write a program to concatenate two tuples.

tuple_1=("ram", "shyam", "krishna", "hari", "hari", "ram", "gita")
tuple_2=(1,2,3,4,5,6,7,8,9,0)

tuple_3=tuple_1+tuple_2
print("concatenated tuple: ",tuple_3)



"""..........................................................................................................................."""



#Find the index of a specific element in a tuple.

tuple_1=("ram", "shyam", "krishna", "hari", "hari", "ram", "gita")
print("index of hari: ",tuple_1.index("hari"))



"""..........................................................................................................................."""


