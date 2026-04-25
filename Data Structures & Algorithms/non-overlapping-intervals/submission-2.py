class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = 0
        prev_end = intervals[0][1]

        for s, e in intervals[1::]:
            if s >= prev_end:
                prev_end = e
            else:
                res += 1
                prev_end = min(e, prev_end)

        return res