class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = left
        for num in range(left, right+1):
            res &= num
            if res == 0:
                return 0

        return res