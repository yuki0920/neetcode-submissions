class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        # dp[i] インデックスiに何ステップで到達できるか
        dp = [float('inf')] * (N)
        dp[0] = 0

        for i in range(N):
            if dp[i] != float('inf') and nums[i] > 0:
                end = min(i+nums[i]+1, N)
                for j in range(i+1, end):
                    dp[j] = min(dp[j], dp[i] + 1)

        return dp[N-1]