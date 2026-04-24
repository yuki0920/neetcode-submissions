class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        carry = 0
        # 一番下の桁から見ていく
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0:
            bit_a = 0
            bit_b = 0
            if i >= 0:
                bit_a = int(a[i])
            if j >= 0:
                bit_b = int(b[j])
            
            total = carry + bit_a + bit_b
            # 1になるのは、bitを足して1か3のとき(0か2のときは0になる)
            char = "1" if total in (1, 3) else "0"
            ans = char + ans
            # 桁上りは、totalが2か3の時のみ起こる
            carry = total // 2
            i -= 1
            j -= 1

        if carry:
            ans = "1" + ans

        return ans

