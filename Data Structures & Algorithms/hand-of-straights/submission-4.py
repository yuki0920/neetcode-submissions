class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        # ソートして選んでいく
        counter = defaultdict(int)
        for h in hand:
            counter[h] += 1

        keys = sorted(counter.keys())

        for key in keys:
            if counter[key] == 0:
                continue

            for i in range(key, key+4):
                counter[i] -= 1
                if counter[i] < 0:
                    return False
        
        return True
