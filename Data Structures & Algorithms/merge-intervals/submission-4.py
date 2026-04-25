class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 開始順でソートする
        intervals.sort(key=lambda x:x[0])

        ans = []
        for s, e in intervals:
            # 始めの候補
            if len(ans) == 0:
                ans.append([s, e])
                continue

            # 始点が最後の終点より小さい場合は、既存の境界と重なっているため、拡張していく
            last_end = ans[-1][1]

            # 重ならない
            if last_end < s:
                ans.append([s, e])
            # 重なる
            else:
                ans[-1][1] = max(last_end, e)

        return ans



            


