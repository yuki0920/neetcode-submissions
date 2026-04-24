class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # インデックスiから見たときの和 or 総和から最小の和を引く

        globMax = float('-inf')
        globMin = float('inf')
        curMax = 0
        curMin = 0
        total = sum(nums)

        for num in nums:
            if curMax < 0:
                curMax = 0
            if curMin > 0:
                curMin = 0

            curMax += num
            globMax = max(globMax, curMax)
            curMin += num
            globMin = min(globMin, curMin)

        return max(globMax, total-globMin)