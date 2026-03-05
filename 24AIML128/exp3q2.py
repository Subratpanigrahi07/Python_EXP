#WRITE A PROGRAM TO INPUT 3 DIFFRENT VALUES AND FIND THE REAL ROOTS.
import math

a =float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("This is not a quadratic equation (a cannot be 0).")
else:
    D = b**2 - 4*a*c
    
    if D > 0:
        root1 = (-b + math.sqrt(D)) / (2*a)
        root2 = (-b - math.sqrt(D)) / (2*a)
        print("Two distinct real roots exist:")
        print("Root 1 =", root1)
        print("Root 2 =", root2)
    elif D == 0:
        root = -b / (2*a)
        print("One real root exists (repeated):")
        print("Root =", root)
    else:
        print("No real roots exist (discriminant < 0).")