"""once you create a tuple, its values can not be changed . tuples are unchangeable and immutable"""
"""but you can change tuple into list, change list and convert list back into tuple"""




"""...................................................change tuple value..............................................................."""

#convert  the tuple into list and change the last item to "sita" and again convert list back into tuple

student_tuple =("ram", "shyam", "krishna", "hari", "hari", "ram", "gita")
print("tuple before: " ,student_tuple)

#converting tuple into list
student_list=list(student_tuple)
print("changed tuple into list: ", student_list)

#changing last item from list
student_list[-1]="sita"

#changing list back into tuple
student_tuple=tuple(student_list)
print("tuple after: " ,student_tuple)

""".............................................................................................................................."""





"""..............................................add item in tuple..........................................................."""
# add "radha" in the student_tuple

student_tuple =("ram", "shyam", "krishna", "hari", "hari", "ram", "gita")
print("tuple before: " ,student_tuple)

student_list=list(student_tuple)
student_list.append("radha")
student_tuple=tuple(student_list)

print("tuple after: ", student_tuple)


"""..........................................................................................................................."""







"""............................................remove item from tuple...................................................."""
# remove shyam from student_tuple

student_tuple =("ram", "shyam", "krishna", "hari", "hari", "ram", "gita")
print("tuple before: " ,student_tuple)

student_list=list(student_tuple)
student_list.remove("shyam")
student_tuple=tuple(student_list)

print("tuple after: ", student_tuple)
