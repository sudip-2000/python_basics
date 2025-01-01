"""......................................list related questions..............................................."""



#Create a list of the first 10 even numbers.

even_list=[2,4,6,8,10,12,14,16,18,20]
print("the list of first 10 even numbers is: ",even_list)




".............................................................................................."



#Write a program to find the largest and smallest numbers in a list.

even_list=[2,4,6,8,10,12,14,16,18,20]
smallest= min(even_list)
largest= max(even_list)

print("the smallest number in the list is: ",smallest)
print("the largest number in the list is: ",largest)



"""..............................................................................................."""


#Reverse a list without using the `reverse()` method.

even_list=[2,4,6,8,10,12,14,16,18,20]   
even_list.sort(reverse=True)
print("the reversed list is: ",even_list)



"""..............................................................................................."""


#Remove duplicates from a list while maintaining the order.

my_list=[2,4,2,3,6,12,6,8,10,12,14,16,18,20,]

unique_list=[]

#using loop to remove duplicates
for x in my_list:
    if x not in unique_list:
        unique_list.append(x)
print(unique_list)


"""..............................................................................................."""


# Write a list comprehension to create a list of squares for numbers 1 to 10.

squares=[x**2 for x in range(1,11)]
print(squares)







