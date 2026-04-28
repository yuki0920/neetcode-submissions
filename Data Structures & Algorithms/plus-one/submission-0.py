class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)
        carry = 1
        for i in range(N-1, -1, -1):
            total = digits[i] + carry
            if total == 10:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
                digits[i] = total

        if carry == 1:
            return [1] + digits
        else:
            return digits

            

