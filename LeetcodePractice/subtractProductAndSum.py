"""
@Time    : 2021/1/9 10:07
@Author  : MD
@File    : subtractProductAndSum.py
"""
"""
给定一个数字n，得到n每位的"乘积"与"和"的差
"""
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # 分别得到积，和
        # 需要先得到每位数字
        sum = 0
        product = 1
        while n > 0:
            sum += n % 10
            product *= n % 10
            n = n // 10
        return product - sum

if __name__ == "__main__":
    so = Solution()
    print(so.subtractProductAndSum(234))