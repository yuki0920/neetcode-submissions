class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        # ソートして選んでいく
        hand.sort()
        counter = defaultdict(int)
        for h in hand:
            counter[h] += 1
        
        first = hand[0]

        while N:
            firstDecided = False
            current = first

            for _ in range(groupSize):
                counter[current] -= 1
                if counter[current] > 0 and not firstDecided:
                    first = current
                    firstDecided = True
                if counter[current] < 0:
                    return False

                current += 1

                N -= 1
            
        
        return True
