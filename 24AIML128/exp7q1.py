# WRITE A PROGRAM TO CREATE A LIST  CONTAINING NATURAL NUMBERS FROM M TO N WHERE M AND N GIVEN INPUT. ( cREATE USING FOR LOOP).
# FIND THE SUM AVG LARGEST AND SMALLEST IN THE LIST.
# CREATE ANOTHER LIST WHICH CONTAINS ALL THREE NUMBERS OF 1ST LIST EXCEPT NUMBERA DIVISEBLE BY 3 

M = int(input("Enter the starting number (M): "))
N = int(input("Enter the ending number (N): "))

numbers = []
for i in range(M, N + 1):
    numbers.append(i)

print("List of numbers:", numbers)

total_sum = sum(numbers)
average = total_sum / len(numbers)
largest = max(numbers)
smallest = min(numbers)

print("Sum:", total_sum)
print("Average:", average)
print("Largest:", largest)
print("Smallest:", smallest)

filtered_list = []
for num in numbers:
    if num % 3 != 0:
        filtered_list.append(num)

print("List excluding numbers divisible by 3:", filtered_list)