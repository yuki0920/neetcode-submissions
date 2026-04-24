class Solution:
    def checkValidString(self, s: str) -> bool:
        # * がない場合、
        # (をスタックに入れ、)が出たらスタックから取り出し、)取り出し時にスタックがからならFalse
        # 最後までループが続けばTrue

        # *は無視して個数を数える。(と)の個数も数える。最後まで探索してその個数の差が、*の個数以内ならクリア

        p_stack = []
        a_stack = []
        N  = len(s)

        for i in range(N):
            if s[i] == "(":
                p_stack.append(i)
            elif s[i] == "*":
                a_stack.append(i)
            else: # )
                if len(p_stack) > 0:
                    p_stack.pop()
                elif len(a_stack) > 0:
                    a_stack.pop()
                else:
                    return False

        # マッチしなかった(の対となる)を*で置き換えられるか検証する。*があとに来ていればマッチできる
        # ex: ((**)
        while p_stack and a_stack:
            if p_stack.pop() > a_stack.pop():
                return False

        return not p_stack
