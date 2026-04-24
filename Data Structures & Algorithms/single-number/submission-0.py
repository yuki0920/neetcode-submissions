class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        
        for i, v in counter.items():
            if v == 1:
                return i