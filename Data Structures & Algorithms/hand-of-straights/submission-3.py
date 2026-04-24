class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        # ソートして選んでいく
        hand.sort()
        counter = defaultdict(int)
        for h in hand:
            counter[h] += 1
        
        first = hand[0]

        for num in hand:
            if counter[num]:
                for i in range(num, num+groupSize):
                    if not counter[i]:
                        return False
                    counter[i] -= 1

        return True
