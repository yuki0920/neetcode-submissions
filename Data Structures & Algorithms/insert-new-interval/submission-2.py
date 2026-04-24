class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)
        ans = []
        for i in range(N):
            s, e = intervals[i]
            ns, ne = newInterval

            # 完全に右 or 左
            if e < ns or ne < s:
                ans.append((s, e))
            # 重なる e >= ns or ne >= s
            else:
                newInterval =  (min(s, ns), max(e, ne))

        ans.append((newInterval[0], newInterval[1]))
        ans.sort()
        return ans