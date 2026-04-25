class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        xor = N
        for i in range(N):
            xor = xor ^ i ^ nums[i]

        return xor