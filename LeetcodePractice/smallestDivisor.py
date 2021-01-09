"""
@Time    : 2021/1/9 10:57
@Author  : MD
@File    : smallestDivisor.py
"""

"""
给定的数组nums，找一个正整数n，使得sum（nums/n）< 阈值x
"""


class Solution:
    def smallestDivisor(self, nums, threshold):
        # 二分查找找到合适的被除数mid
        left, right, res = 1, max(nums) + 1, -1
        while left <= right:
            mid = (left + right) // 2
            total = sum((num - 1) // mid + 1 for num in nums)
            if total > threshold:
                # 如果结果和大于阈值，应该找更小的结果，应该增大mid
                left = mid + 1
            else:
                # total < threshold，符合要求，找到最大和，减小mid
                res = mid
                right = mid - 1
        return res


if __name__ == '__main__':
    so = Solution()
    print(so.smallestDivisor([2, 3, 5, 7, 11], 11))
