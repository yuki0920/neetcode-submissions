class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 共通の上位ビットのみを探す

        shift = 0
        # left == rightになったら停止する
        # left == rightのとき、bitが共通している
        while left < right:
            left >>= 1 
            right >>= 1 
            shift += 1
        return left << shift