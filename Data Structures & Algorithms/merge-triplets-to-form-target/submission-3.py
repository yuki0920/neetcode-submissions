class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # x, y, zの順に合わせていく
        # xをあわせた時点で、y, zが超過したら次の候補に行き、さいごまで超過したらFalse
        # yをあわせた時点でzが超過したら次の候補に行き、さいごまで超過したらFalse
        # zを合わせるためには、x, yが完全一致するものを選ぶ

        a_list = []
        b_list = []
        c_list = []
        N = len(triplets)
        for i in range(N):
            if triplets[i][0] == target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                a_list.append(i)
            if triplets[i][1] == target[1] and triplets[i][0] <= target[0] and triplets[i][2] <= target[2]:
                b_list.append(i)
            if triplets[i][2] == target[2] and triplets[i][0] <= target[0] and triplets[i][1] <= target[1]:
                c_list.append(i)

            if triplets[i] == target:
                return True

        # a, b, cいずれのリストもあれば作ることができる
        return True if a_list and b_list and c_list else False