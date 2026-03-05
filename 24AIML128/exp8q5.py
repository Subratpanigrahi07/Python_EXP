# WRITE A FUNCTION TO CHECH WEATHER A NUMBER IS PRIME.

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print(is_prime(2))   
print(is_prime(15)) 
print(is_prime(17)) 