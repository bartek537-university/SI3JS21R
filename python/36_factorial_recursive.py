def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Cannot calculate factorial of negative values.")
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
