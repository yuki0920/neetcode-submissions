class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # 開始時刻でソートする
        # 部屋を表すリストを複数用意する。部屋ごとのstart, endを管理する

        meetings.sort(key=lambda x: x[0])
        ends = [0] * n
        counter = [0] * n
        for s, e in meetings:
            found = False
            min_room = 0
            # 既存の部屋に待ち無しで入れるかを確認する
            # この過程で一番終わりが早い部屋とその時間を探す
            for i in range(len(ends)):
                if s >= ends[i]:
                    ends[i] = e
                    counter[i] += 1
                    found = True
                    break
                elif ends[i] < ends[min_room]:
                    min_room = i

            # 待ち無しで部屋が見つからなかった場合は、一番早い終了時刻の部屋を使い、終了時刻を元の会議時間(e-s)分プラスする
            if not found:
                ends[min_room] += (e - s)
                counter[min_room] += 1

        max_count = float('-inf')
        max_index = None

        for i in range(len(counter)):
            if counter[i] > max_count:
                max_count = counter[i]
                max_index = i

        return max_index

                    
