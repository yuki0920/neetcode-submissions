class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dicts = {}
        for i in range(25):
            char = chr(ord('A') + i) 
            dicts[i+1] = char
        dicts[0] = 'Z'
        ans = ''
        while True:
            q, mod = divmod(columnNumber, 26)
            ans = dicts[mod] + ans

            if q == 0 or (q == 1 and mod == 0):
                break

            columnNumber = q

        return ans
