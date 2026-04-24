"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # 終了時間でソートし、未処理のリストに入れる
        # 同じミーティングループで対応できるものは処理し、できないものは再びリストに入れる
        intervals.sort(key=lambda i: i.end)
        ans = 0

        while intervals:
            new_intervals = []
            prev_end = 0
            for interval in intervals:
                if interval.start < prev_end:
                    new_intervals.append(interval)
                else:
                    prev_end = interval.end

            intervals = new_intervals
            ans += 1

        return ans



