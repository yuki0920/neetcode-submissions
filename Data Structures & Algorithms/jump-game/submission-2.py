class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        # dp[i] インデックスiに到達可能かどうか
        dp = [False] * (N+1)
        dp[0] = True

        for i in range(N):
            if dp[i] and nums[i] > 0:
                for j in range(i, min(i+nums[i]+1, N)):
                    dp[j] = True

        return dp[N-1]
