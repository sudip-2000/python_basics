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
