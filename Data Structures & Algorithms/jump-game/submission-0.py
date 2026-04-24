class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        # dp[i] インデックスiに到達可能かどうか
        dp = [False] * (N+1)
        dp[0] = True

        for i in range(N):
            if dp[i]:
                dp[i+nums[i]] = True

        return dp[N-1]
