class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        next_bit = 0
        num = 0
        for n in nums:
            if n & 1 != next_bit:
                return num

            num += 1
            if next_bit == 1:
                next_bit = 0
            else:
                next_bit = 1