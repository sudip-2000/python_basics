""" Write a Python program to simulate a simple grading system:
 Score >= 90: Print "A"
 Score >= 80: Print "B"
 Score >= 70: Print "C"
 Score >= 60: Print "D"
 Score < 60: Print "F"
"""
score = int(input("Enter your score:"))

if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")