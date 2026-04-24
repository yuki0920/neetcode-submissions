class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # 開始時刻でソートする
        # 部屋を表すリストを複数用意する。部屋ごとのstart, endを管理する

        meetings.sort(key=lambda x: x[0])
        ends = [0] * n
        counter = [0] * n
        for s, e in meetings:
            found = False
            min_end = float('inf')
            min_end_index = None
            # 既存の部屋に待ち無しで入れるかを確認する
            # この過程で一番終わりが早い部屋とその時間を探す
            for i in range(len(ends)):
                if s >= ends[i]:
                    ends[i] = e
                    counter[i] += 1
                    found = True
                    break
                elif ends[i] < min_end:
                    min_end = ends[i]
                    min_end_index = i


            if not found:
                ends[min_end_index] += (e - s)
                counter[min_end_index] += 1

        max_count = float('-inf')
        max_index = None

        for i in range(len(counter)):
            if counter[i] > max_count:
                max_count = counter[i]
                max_index = i

        return max_index

                    
