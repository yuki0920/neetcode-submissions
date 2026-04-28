class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        nums = list(str(n))
        count = 0
        while True:
            s = sum(int(num) ** 2 for num in nums)
            if s == 1:
                return True
            elif s in seen:
                return False

            seen.add(s)
            nums = list(str(s))