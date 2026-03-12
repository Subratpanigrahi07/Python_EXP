#   WAP TO PRINT EVEN LENGH WORDS IN A STRING
x = input("Enter a string:")
y=""
for c in x:
   if c !="":
     y=y+c
   ekse:
   if len(y)%2 == 0:
      print(y)
    y=""
if len(y)%2 == 0:
   print(y)
y=""
if len(y)%2 == 0:
   print(y)