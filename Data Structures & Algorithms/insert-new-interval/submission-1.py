class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)
        ans = []
        for i in range(N):
            s, e = intervals[i]
            ns, ne = newInterval

            if e < ns:
                ans.append((s, e))
            elif s <= ne:
                newInterval =  (min(s, ns), max(e, ne))
            else:
                ans.append((s, e))
        ans.append((newInterval[0], newInterval[1]))
        ans.sort()
        return ans