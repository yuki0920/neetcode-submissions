class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        N = len(s)
        # dp[i] インデックスiに到達可能かどうか
        dp = [False] * (N)
        dp[0] = True

        for i in range(N):
            if dp[i]:
                start = min(i+minJump, N)
                end = min(i+maxJump+1, N)
                for j in range(start, end):
                    if s[j] == '0':
                        dp[j] = True

        return dp[N-1]