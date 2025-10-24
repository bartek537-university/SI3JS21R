class Math:
    @staticmethod
    def _multiplied(x: float, n: int) -> float:
        if n < 1:
            return 0
        result = 1
        for i in range(n):
            result *= x
        return result

    @staticmethod
    def pow(x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x

        return Math._multiplied(x, abs(n))


print(Math.pow(2, 0))
print(Math.pow(2, 1))
print(Math.pow(2, 5))
print(Math.pow(2, -5))
