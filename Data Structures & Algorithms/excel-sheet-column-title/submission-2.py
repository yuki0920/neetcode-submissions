class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber > 0:
            columnNumber -= 1

            q, mod = divmod(columnNumber, 26)
            ans = chr(ord('A') + mod) + ans

            columnNumber = q

        return ans
