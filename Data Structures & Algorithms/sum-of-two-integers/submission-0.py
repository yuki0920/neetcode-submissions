class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = 0
        an = 0
        bn = 0
        while a:
            if a & 1 == 1:
                ans += 2 ** an
            an += 1
            a = a >> 1

        while b:
            if b & 1 == 1:
                ans += 2 ** bn
            bn += 1
            b = b >> 1

        return ans
