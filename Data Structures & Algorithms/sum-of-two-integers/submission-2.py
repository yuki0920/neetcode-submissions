class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = False
        res = 0
        mask = 0xFFFFFFFF
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1

            # 現在のビットは、3つすべて1か、1つだけ1のときだけ立つ
            cur_bit = a_bit ^ b_bit ^ carry
            carry = a_bit + b_bit + carry >= 2
            res |= (cur_bit << i)

        # 0x7FFFFFFF(01111111 11111111 11111111 11111111) == 2 ** 32 - 1
        if res > 0x7FFFFFFF:
            # 0xFFFFFFFF(01111111 11111111 11111111 11111111)を使い、32bitでの負の数を、Pythonの負の数に変換している
            res = ~(res ^ mask)

        return res

