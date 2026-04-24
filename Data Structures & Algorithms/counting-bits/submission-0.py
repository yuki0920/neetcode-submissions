class Solution:
    def countBits(self, n: int) -> List[int]:
        def countBit(n) -> int:
            count = 0
            while n > 0:
                if n & 1:
                    count += 1
                n = n >> 1
            
            return count

        ans = []
        for i in range(n+1):
            ans.append(countBit(i))

        return ans

