class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for s, e in intervals:
            # 始めの候補
            if len(ans) == 0:
                ans.append([s, e])
            # 重ならない
            elif ans[-1][1] < s:
                ans.append([s, e])
            # 加算る
            else:
                # ans[-1][0] = min(ans[-1][0], s)
                ans[-1][1] = max(ans[-1][1], e)

        return ans



            


