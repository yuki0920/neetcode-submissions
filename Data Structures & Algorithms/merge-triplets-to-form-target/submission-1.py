class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # x, y, zの順に合わせていく
        # xをあわせた時点で、y, zが超過したら次の候補に行き、さいごまで超過したらFalse
        # yをあわせた時点でzが超過したら次の候補に行き、さいごまで超過したらFalse
        # zを合わせるためには、x, yが完全一致するものを選ぶ

        a_que = []
        b_que = []
        c_que = []
        N = len(triplets)
        for i in range(N):
            if triplets[i][0] == target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                a_que.append(i)
            if triplets[i][1] == target[1] and triplets[i][0] <= target[0] and triplets[i][2] <= target[2]:
                b_que.append(i)
            if triplets[i][2] == target[2] and triplets[i][0] <= target[0] and triplets[i][1] <= target[1]:
                c_que.append(i)

            if triplets[i] == target:
                return True

        for i in a_que:
            current = triplets[i]

            for j in b_que:                
                b = triplets[j]
                current = [
                    max(current[0], b[0]),
                    max(current[1], b[1]),
                    max(current[2], b[2]),
                ]
                if current == target:
                    return True
                
                for k in c_que:
                    c = triplets[k]
                    current = [
                        max(current[0], c[0]),
                        max(current[1], c[1]),
                        max(current[2], c[2]),
                    ]
                    if current == target:
                        return True                

        return False