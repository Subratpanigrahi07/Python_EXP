#WAP TO CHECK WHEATHER THE STRING IS SYMETRUCAL OR PELINDROME

x=input("Enter a string : ")
z=(str(str(x)[::-1]))
if x == z:
    print("it is a pelindrpme")
else:
    print("it is not a pelindrome")