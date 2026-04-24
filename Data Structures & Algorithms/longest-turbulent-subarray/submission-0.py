class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # turbulentな場合の2つのパターンのうち、1つを検証する(奇数のインデックスが偶数のインデックスより大きくなること)
        N = len(arr)
        prev = arr[0]
        cur_max_odd = 1
        cur_max_even = 1
        length_max = 1
        for i in range(1, N):
            num = arr[i]
            mod = i % 2

            if num == prev:
                cur_max_odd = 1
                cur_max_even = 1

            if mod == 0:
                if num < prev:
                    cur_max_odd += 1
                    cur_max_even = 1
                elif num > prev:
                    cur_max_even += 1
                    cur_max_odd = 1
            else:
                if num > prev:
                    cur_max_odd += 1
                    cur_max_even = 1
                elif num < prev:
                    cur_max_even += 1
                    cur_max_odd = 1

            length_max = max(length_max, cur_max_odd, cur_max_even)
            
            prev = arr[i]

        
        return length_max
