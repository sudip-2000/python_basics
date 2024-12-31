"""when we create a tuple, we normally assign values to it. this is called "packing" a tuple"""
"""but in python be can extract the values back into variables which is called unpacking"""

#unpacking tuple
name=("ram", "shyam", "sita")
(roll_1, roll_2, roll_3)= name
print(roll_1)
print(roll_2)
print(roll_3)


"""................................................................................"""


"""if no. of variables is less than number of values, you can add * to the variable name
and the value will be assigned to the variable as a list"""


#assign rest to values as a list called "rest":
student_name=("ram", "shyam", "sita", "gita", "hari")
(id_1, id_2, *id_3)=student_name
print(id_1)
print(id_2)
print(id_3)




