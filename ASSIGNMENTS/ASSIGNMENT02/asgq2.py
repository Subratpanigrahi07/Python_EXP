# 2. WAP to enter a 5 digit number and print the digits present at odd locations. 

I=[]
x=int(input("Enter a 5 digit number:"))
while(x!=0):
 y=x%10
 x=int(x/10)
 I.append(y)
print("Numbers at odd postion :")
for i in range(len(I)-1,-1,-2):
 print(I[i])
