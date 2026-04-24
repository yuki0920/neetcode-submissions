class Solution:
    def checkValidString(self, s: str) -> bool:
        # * がない場合、
        # (をスタックに入れ、)が出たらスタックから取り出し、)取り出し時にスタックがからならFalse
        # 最後までループが続けばTrue

        # *は無視して個数を数える。(と)の個数も数える。最後まで探索してその個数の差が、*の個数以内ならクリア

        left_counter = 0
        right_counter = 0
        a_counter = 0
        N = len(s)
        for i in range(N):
            if s[i] == "(":
                left_counter += 1
            elif s[i] == ")":
                right_counter -= 1
            else:
                a_counter += 1

            if (right_counter - left_counter) > a_counter:
                return False

        return abs(left_counter) <= a_counter