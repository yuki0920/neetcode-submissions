class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""
        while n > 0:
            if n & 1 == 1:
                binary += "1"
            else:
                binary += "0"
            n = n >> 1

        binary = "0" * (32 - len(binary)) + binary
        binary = binary[::-1]

        print(binary)

        res = 0
        for i in range(32):
            s = int(binary[i])
            if s & 1 == 1:
                res += 2 ** (31 - i)

        return res
