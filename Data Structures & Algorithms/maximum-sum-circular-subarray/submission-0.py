class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 配列の最大部分和
        globMax = nums[0]
        # 配列の最小部分和
        globMin = nums[0]
        # 今の位置で終わる最大部分和
        curMax = 0
        # 今の位置で終わる最小部分和
        curMin = 0
        # 配列全体の和
        total = 0

        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            total += num
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)
            print("max", globMax, curMax)
            print("min", globMin, curMin)

        # globMaxが負のときは、配列の全要素が負なので、max(globMax, total-glob)が0となり空列を返すため、globMaxを返す
        return max(globMax, total - globMin) if globMax > 0 else globMax
