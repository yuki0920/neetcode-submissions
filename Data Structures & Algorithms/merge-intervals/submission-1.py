class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        starts = defaultdict(int)
        ends = defaultdict(int)
        for interval in intervals:
            s, e = interval
            starts[s] += 1
            ends[e] += 1

        ans = []
        start_stack = []
        
        for i in range(1001):
            if i in starts:
                for _ in range(starts[i]):
                    start_stack.append(i)
            if i in ends:
                for _ in range(ends[i]):
                    s = start_stack.pop()
                    if len(start_stack) == 0:
                        ans.append([s, i])

        return ans


            


