class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2:][::-1]
        N = len(bits)
        num = int(bits + '0' * (32-N), 2)
    
        return num