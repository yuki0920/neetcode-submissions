class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 何回連続でレートが上がっているかをチェックする
        high_i = 0
        low_i = 0
        diff = 0
        prev = ratings[0]
        N = len(ratings)
        for i in range(1, N):
            current = ratings[i]
            if current > prev:
                high_i = i
                diff += (i - low_i )
            elif current < prev:
                low_i = i
                diff += (i - high_i)
            prev = current

        return diff+N