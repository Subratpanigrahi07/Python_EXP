#GENERATE A FABONACI SERIES BETWEEN 0 TO 100 THEN FIND THE SUM OF EVEN VALUED TERMS
fibonacci = [0, 1]
while fibonacci[-1] + fibonacci[-2] <= 100:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print("Fibonacci series between 0 and 100:")
print(fibonacci)

even_sum = sum([num for num in fibonacci if num % 2 == 0])
print("Sum of even-valued terms:", even_sum)
