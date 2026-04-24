class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        rest = []
        intervals.sort()
        for s, e in intervals:
            if not rest:
                rest.append([s, e])
            elif s >= rest[-1][1]:
                rest.append([s, e])
                

        return len(intervals) - len(rest)