class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # 先行が有利。
        # かつ自分のすぐ右を使えなくするのが良い
        N = len(senate)
        banned = [False] * N
        s_banned = True
        r_banned = True
        while s_banned or r_banned:
            s_banned = False
            r_banned = False
            for i in range(N):
                # Rはバンされていないとき、Sをバンする
                if senate[i] == "R" and not banned[i]:
                    for j in range(i+1, i+N+1):
                        k = j % N
                        if senate[k] == "S" and not banned[k]:
                            banned[k] = True
                            s_banned = True
                # Sはバンされていないとき、Rをバンする
                elif senate[i] == "S" and not banned[i]:
                    for j in range(i+1, i+N+1):
                        k = N % j
                        if senate[k] == "R" and not banned[k]:
                            banned[k] = True
                            r_banned = True

        for i in range(N):
            if not banned[i]:
                if senate[i] == "R":
                    return "Radiant"
                else:
                    return "Dire"
