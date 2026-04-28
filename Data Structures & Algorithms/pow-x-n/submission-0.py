class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(x, n) -> float:
            if n == 0:
                return 1
            if n >= 1:
                return rec(x, n-1) * x
            else:
                return rec(x, n+1) / x

        return rec(x, n)