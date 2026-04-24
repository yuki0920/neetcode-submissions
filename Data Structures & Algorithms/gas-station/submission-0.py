class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)

        for i in range(N):
            # スタート地点でガスよりコストが大きいと移動できない
            if gas[i] < cost[i]:
                continue

            cur_gas = gas[i]
            for j in range(N):
                k = (i+j) % N
                cur_gas -= cost[k]
                # 移動してガスがマイナスになったら終わり
                if cur_gas < 0:
                    break
                l = (i+j+1) % N
                cur_gas += gas[l]

            if cur_gas >= 0:
                return i

        return -1