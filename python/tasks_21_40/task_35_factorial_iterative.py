def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Cannot calculate factorial of negative values.")
    if n == 0:
        return 1
    for i in range(1, n):
        n *= i
    return n


print(factorial(5))
