class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = defaultdict(int)
        for bill in bills:
            if bill == 5:
                changes[5] += 1
            elif bill == 10:
                changes[10] += 1
                changes[5] -= 1
            else: # bill == 20
                if changes[10] > 0:
                    changes[10] -= 1
                    changes[5] -= 1
                else:
                    changes[5] -= 3
                changes[20] += 1

            if changes[5] < 0 or changes[10] < 0:
                return False

        return True
