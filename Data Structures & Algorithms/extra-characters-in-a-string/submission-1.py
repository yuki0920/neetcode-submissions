class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # dp[i]: i文字目までを追加の文字数X個で作れる
        N = len(s)
        dp = [float('inf')] * (N+1)
        dp[0] = 0
        # 先頭文字ごとの辞書
        dicts = defaultdict(list)
        for d in dictionary:
            dicts[d[0]].append(d)

        for i, c in enumerate(s):
            if c in dicts:
                for word in dicts[c]:
                    n = len(word)
                    if s[i:i+n] == word:
                        dp[i+n] = dp[i]
            dp[i+1] = min(dp[i+1], dp[i]+1)

        return dp[N]

