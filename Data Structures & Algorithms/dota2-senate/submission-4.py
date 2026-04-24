class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # 先行が有利。
        # かつ自分のすぐ右を使えなくするのが良い
        N = len(senate)
        r_que = deque()
        d_que = deque()

        for i in range(N):
            if senate[i] == "R":
                r_que.append(i)
            else:
                d_que.append(i)


        while r_que and d_que:
            r = r_que.popleft()
            d = d_que.popleft()

            # インデックス番号が小さい方が勝ち、他方を無効化する
            if r < d:
                r_que.append(r+N)
            else:
                d_que.append(d+N)

        return "Radiant" if r_que else "Dire"
