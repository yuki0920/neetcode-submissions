class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        # startが小さい順に隠していく
        for s, e in intervals:
            ns, ne = newInterval
            # ターゲットが完全に左
            if e < ns:
                ans.append([s, e])
            # ターゲットが完全に右
            elif s > ne:
                # ターゲットをansに追加し、既存のをターゲットとする
                ans.append(newInterval)
                newInterval = [s, e]
            # 重なる
            else:
                newInterval = [min(s, ns), max(e, ne)]

        ans.append(newInterval)
        
        return ans
        