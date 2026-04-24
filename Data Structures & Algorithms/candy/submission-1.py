class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)

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
            if current > ne:
                candies[i] = candies[i+1] + 1

        print(candies)

        return sum(candies)

    

