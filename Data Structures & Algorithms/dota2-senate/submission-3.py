class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # 先行が有利。
        # かつ自分のすぐ右を使えなくするのが良い
        N = len(senate)
        banned = [False] * N
        changed = True
        last_banner = None

        while changed:
            changed = False
            for i in range(N):
                if banned[i]:
                    continue

                # Rはバンされていないとき、Sをバンする
                if senate[i] == "R":
                    for j in range(i+1, i+N+1):
                        k = j % N
                        if senate[k] == "D" and not banned[k]:
                            banned[k] = True
                            changed = True
                            last_banner = "Radiant"
                            break
                # Sはバンされていないとき、Rをバンする
                elif senate[i] == "D":
                    for j in range(i+1, i+N+1):
                        k = j % N
                        if senate[k] == "R" and not banned[k]:
                            banned[k] = True
                            changed = True
                            last_banner = "Dire"
                            break

        if last_banner:
            return last_banner
        
        for i in range(N):
            if not banned[i]:
                if senate[i] == "R":
                    return "Radiant"
                else:
                    return "Dire"
