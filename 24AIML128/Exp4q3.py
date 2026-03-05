# WRITE A PROGRAM TO FIND THE GCD OF THRREE NUMBERS

import math
def gcd_three(a, b, c):
    return math.gcd(math.gcd(a, b), c)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
result = gcd_three(num1, num2, num3)
print(f"The GCD of {num1}, {num2}, and {num3} is: {result}")