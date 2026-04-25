"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # 開始時間でソートし、未処理のリストに入れる
        # 同じミーティングループで対応できるものは処理し、できないものは再びリストに入れる
        intervals.sort(key=lambda i: i.start)
        ans = 0

        new_rooms = [intervals[0]]
        for interval in intervals[1::]:
            diff_min = float('inf')
            diff_min_i = None
            for i in range(len(new_rooms)):
                room_interval = new_rooms[i]
                diff = interval.start - room_interval.end  
                if diff >= 0 and diff < diff_min:
                    diff_min = diff
                    diff_min_i = i

            if diff_min_i:
                new_rooms[diff_min_i] = [interval]
            else:
                new_rooms.append(interval)

        return len(new_rooms)
                    




