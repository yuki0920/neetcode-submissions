class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        rest = []
        intervals.sort(key=lambda x: x[1])

        for s, e in intervals:
            if not rest:
                rest.append([s, e])
                continue

            last_end = rest[-1][1]
            if s >= last_end:
                rest.append([s, e])

        return len(intervals) - len(rest)