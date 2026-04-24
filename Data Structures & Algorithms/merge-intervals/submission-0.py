class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        newInterval = (intervals[0][0], intervals[0][1])
        N = len(intervals)
        ans = []
        for i in range(1, N):
            s, e = intervals[i]
            ns, ne = newInterval

            # 完全に右 or 左
            if e < ns or ne < s:
                ans.append((s, e))
            else:
                newInterval = (min(s, ns), max(e, ne))

        ans.append(newInterval)
        ans.sort()

        return list(ans)
