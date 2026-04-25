class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)

        # まずは左から右へ、左より多ければアメを増やしてあげていく
        # 次に右から左へ、右より多ければアメを増やしてあげていく。しかし、すでに右よりも多い場合は、増やさない

        candies = [1] * N
        # 左から右に走査し、左より大きいか確認するする
        for i in range(1, N):
            prev = ratings[i-1]
            current = ratings[i]
            if current > prev:
                candies[i] = candies[i-1] + 1

        # 右から左に走査し、右より大きいか確認するする
        for i in range(N-2, -1, -1):
            current = ratings[i]
            ne = ratings[i+1]
            # 右よりレートが高い場合
            if current > ne:
                # 右よりレートが高くても、すでに右よりアメの数が多い場合は、アメは増やさなくてよい
                candies[i] = max(candies[i], candies[i+1]+1)


        return sum(candies)

    

