# WRITE A PROGRAM TO FIND THE SUM OF DIGITS OF A POSITIVE INTIGER


def sum_of_digits(num: int) -> int:
    """
    Returns the sum of digits of a positive integer.
    """
    if num < 0:
        raise ValueError("Number must be positive")
    
    total = 0
    while num > 0:
        total += num % 10  
        num //= 10          
    return total

if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    print("Sum of digits:", sum_of_digits(n))