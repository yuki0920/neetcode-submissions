class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(x, n) -> float:
            if n == 0:
                return 1
            if 1 <= n <= 2:
                return rec(x, n-1) * x
            elif -1 <= n <= 2:
                return rec(x, n+1) / x
            elif n > 2:
                a = n // 2
                b = n - a
                return rec(x, a-1) * rec(x, b-1) * x * x
            else: # n < -12
                a = n // 2
                b = n - a
                return rec(x, a+1) * rec(x, b+1) / x / x
                

        return rec(x, n)