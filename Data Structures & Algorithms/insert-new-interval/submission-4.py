class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # マージ操作は左から順に処理したい->start起点で並び替える
        # マージしに、新しい境界を拡張していく

        intervals.sort(key=lambda x:x[0])
        ans = []
        ns, ne = newInterval

        for s, e in intervals:
            # 完全に左
            if e <= ns:
                ans.append([s, e])
            # 完全に右
            elif s >= ne:
                ans.append([s, e])
            # 重なる
            else:
                ns = min(ns, s)
                ne = max(ne, e)

        ans.append([ns, ne])

        ans.sort(key=lambda x:x[0])

        return ans


