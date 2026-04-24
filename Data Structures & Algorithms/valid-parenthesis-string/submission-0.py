class Solution:
    def checkValidString(self, s: str) -> bool:
        # * がない場合、
        # (をスタックに入れ、)が出たらスタックから取り出し、)取り出し時にスタックがからならFalse
        # 最後までループが続けばTrue

        # *は無視して個数を数える。(と)の個数も数える。最後まで探索してその個数の差が、*の個数以内ならクリア

        p_counter = 0
        a_counter = 0
        N = len(s)
        for i in range(N):
            if s[i] == "(":
                p_counter += 1
            elif s[i] == ")":
                p_counter -= 1
            else:
                a_counter += 1

        return abs(p_counter) <= a_counter