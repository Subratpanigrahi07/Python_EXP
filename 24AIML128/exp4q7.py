# PRINT FABONACI SERIES UP TO N TERMS

def fibonacci(n: int) -> list[int]:
    """
    Return the Fibonacci series up to n terms.
    n must be a non-negative integer.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return []
    if n == 1:
        return [0]

    series = [0, 1]
    for _ in range(2, n):
        series.append(series[-1] + series[-2])
    return series

if __name__ == "__main__":
    try:
        n = int(input("Enter number of terms (n): "))
        print("Fibonacci series:", fibonacci(n))
    except ValueError as e:
        print("Invalid input:", e)