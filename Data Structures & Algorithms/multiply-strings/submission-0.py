class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len1 = len(num1)
        len2 = len(num2)

        ans = 0
        init = 1
        for i in range(len1-1, -1, -1):
            carry = 1
            for j in range(len2-1, -1, -1):
                ans += int(num2[j]) * int(num1[i]) * carry * init
                carry *= 10

            init *= 10

        return str(ans)