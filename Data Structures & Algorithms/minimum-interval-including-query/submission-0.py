class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # 1000 * 1000 なので、bruteforceで考える
        ans = []
        for q in queries:
            min_d = float('inf')

            for i in range(len(intervals)):
                s, e = intervals[i]
                d = e - s + 1

                if  s <= q <= e and d < min_d:
                    min_d = d

            if min_d != float('inf'):
                ans.append(min_d)
            else:
                ans.append(-1)

        return ans

