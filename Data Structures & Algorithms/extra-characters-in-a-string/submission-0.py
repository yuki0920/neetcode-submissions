class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # dp[i]: i文字目まで作れる
        N = len(s)
        dp = [False] * (N+1)
        dp[0] = True
        # 先頭文字ごとの辞書
        dicts = defaultdict(list)
        for d in dictionary:
            dicts[d[0]].append(d)

        for i, c in enumerate(s):
            if not dp[i]:
                continue

            if c in dicts:
                for word in dicts[c]:
                    n = len(word)
                    if s[i:i+n] == word:
                        dp[i+n] = True

        ans = N - max(i for i in range(len(dp)) if dp[i])
        return ans

