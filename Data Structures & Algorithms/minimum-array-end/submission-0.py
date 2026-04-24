class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # xと&してxになる値を小さい順にxからn個並べ、最後の要素を返せば良い
        ans = 1
        num = x
        while ans < n:
            num += 1
            if num & x == x:
                ans += 1

        return num
