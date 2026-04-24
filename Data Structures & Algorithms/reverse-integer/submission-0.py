class Solution:
    def reverse(self, x: int) -> int:
        s = 0
        if x >= 0:
            s = int(str(x)[::-1])
        else:
            s = int(str(x)[1:][::-1]) * -1

        
        if 2 ** 31 * -1 <= s <= 2 ** 31 - 1:
            return s
        else:
            return 0