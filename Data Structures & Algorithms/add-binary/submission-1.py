class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        countup = 0
        count = 0
        a = a[::-1]
        b = b[::-1]
        A = len(a)
        B = len(b)
        i = 0
        j = 0

        while i < A or j < B:
            if i < A and j < B:
                if countup + int(a[i]) + int(b[j]) == 3:
                    countup = 1
                    ans = "1" + ans
                elif countup + int(a[i]) + int(b[j]) == 2:
                    countup = 1
                    ans = "0" + ans
                elif countup + int(a[i]) + int(b[j]) == 1:
                    ans = "1" + ans
                    countup = 0
                else:
                    ans = "0" + ans
                    countup = 0
            elif i < A:
                if countup + int(a[i]) == 2:
                    countup = 1
                    ans = "0" + ans
                elif countup + int(a[i]) == 1:
                    ans = "1" + ans
                    countup = 0
                else:
                    ans = "0" + ans
                    countup = 0
            else:
                if countup + int(b[j]) == 2:
                    countup = 1
                    ans = "0" + ans
                elif countup + int(b[j]) == 1:
                    ans = "1" + ans
                    countup = 0
                else:
                    ans = "0" + ans
                    countup = 0


            if i < A:
               i += 1 
            if j < B:
                j += 1

            count += 1

        if countup:
            ans = "1" + ans

        return ans

