class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)

        for i in range(N):
            # スタート地点でガスよりコストが大きいと移動できない
            if gas[i] < cost[i]:
                continue

            tank = 0
            for j in range(N):
                k = (i+j) % N
                tank += gas[k]
                tank -= cost[k]
                if tank < 0:
                    break

            if tank >= 0:
                return i

        return -1