#WRITE A PROGRAM TO CREATE OR EMPTY LIST AND INPUT A GROUP OF NUMBERS INTO THE LIST, REMOVE DUPLICATE ELEMENTS FROM IT AND THEN SENT THEM ASENDING ORDER THEN DISPLAY

numbers = []

n = int(input("Enter how many numbers you want to input: "))
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("\nOriginal List:", numbers)

unique_numbers = list(set(numbers))

unique_numbers.sort()

print("List after removing duplicates and sorting:", unique_numbers)