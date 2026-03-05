# WRITE A PROGRAM TO GENERATE ALL PRIME NUMBERS WITHIN A GIVEN RANGE FROM M TO N

M = int(input("Enter the starting number (M): "))
N = int(input("Enter the ending number (N): "))

print(f"Prime numbers between {M} and {N} are:")

for num in range(M, N + 1):
    if num > 1:  
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")