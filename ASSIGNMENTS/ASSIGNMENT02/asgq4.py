# 4. WAP to enter a number and check whether the number is perfect number or not. 

x=int(input("enter a number:"))
s=0
for i in range(1,x):
 if(x%i==0):
  s=s+i
 if(s==x):
   print("It is a perfect number")
else:
   print("It is not a perfect number")
