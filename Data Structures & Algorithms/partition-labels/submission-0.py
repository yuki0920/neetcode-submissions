class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # letterごとのインデックスを保存する
        # left, rightをずらしていく
        N = len(s)
        C = {}
        for i in range(N):
            C[s[i]] = i
        print(C)
        R = C[s[0]]
        L = 0
        ans = []
        for i in range(N):
            # 他にも文字が含まれるとき右端を拡張する
            if i > R:
                ans.append(R-L+1)
                L = i

            R = max(R, C[s[i]])

        ans.append(R-L+1)

        return ans

