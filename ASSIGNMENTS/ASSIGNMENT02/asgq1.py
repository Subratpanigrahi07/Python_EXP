# 1. WAP to enter a percentage and display the gradation system. 

x=int(input("enter the percentage:"))
if x>=90:
 print("the equivalent grade is 'O'")
elif x>=80 and x<90:
 print("the equivalent grade is 'E'")
elif x>=70 and x<80:
 print("the equivalent grade is 'A'")
elif x>=60 and x<70:
 print("the equivalent grade is 'B'")
elif x>=50 and x<60:
 print("the equivalent grade is 'C'")
elif x>=40 and x<50:
 print("the equivalent grade is 'D'")
else:
 print("the equivalent grade is 'F'")