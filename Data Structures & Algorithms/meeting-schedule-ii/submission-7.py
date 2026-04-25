"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # 開始時間でソートし、順に処理をする
        # 既存の部屋で対応できる場合、一番効率の良い方法(開始時間と終了時間の差が少ないところ)で割り当てる
        # 対応できない場合は、新しい部屋に追加する
        intervals.sort(key=lambda i: i.start)
        # 終了時間を早い順に入れる部屋
        min_heap = []

        for interval in intervals:
            # 一番終了時間が早い部屋: min_heap[0]
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)




