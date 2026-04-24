class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # 先行が有利。
        # かつ自分のすぐ右を使えなくするのが良い
        N = len(senate)
        senates = list(senate)

        while True:
            changed = False
            for i in range(N):
                # LosedなものはLとマーキングする
                if senates[i] == "L":
                    continue

                target = "D" if senates[i] == "R" else "R"

                for j in range(i+1, i+N):
                    k = j % N
                    if senates[k] == "L":
                        continue

                    if senates[k] == target:
                        senates[k] = "L"
                        changed = True
                        break

                    return "Radiant" if senates[i] == "R" else "Dire"

            if not changed:
                break
        
        for s in senates:
            if s != "L":
                return "Radiant" if s == "R" else "Dire"
