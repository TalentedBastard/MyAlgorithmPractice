"""
@Time    : 2021/1/9 11:41
@Author  : MD
@File    : test.py
"""






class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:



        l, r, ans = 1, max(nums) + 1, -1
        while l <= r:
            mid = (l + r) // 2
            total = sum((x - 1) // mid + 1 for x in nums)
            if total <= threshold:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
