class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dicts = {}
        for i in range(26):
            char = chr(ord('A') + i) 
            dicts[i+1] = char

        ans = ""
        while True:
            q, mod = divmod(columnNumber, 26)
            ans = dicts[mod] + ans

            if q == 0:
                break

            columnNumber = q

        return ans
