class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)
        plus_one = 1
        for i in range(N-1, -1, -1):
            total = digits[i] + plus_one
            if total == 10:
                plus_one = 1
                digits[i] = 0
            else:
                plus_one = 0
                digits[i] = total

        if plus_one == 1:
            return [1] + digits
        else:
            return digits

            

