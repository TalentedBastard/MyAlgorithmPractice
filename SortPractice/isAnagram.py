"""
@Time    : 2020/12/27 21:44
@Author  : MD
@File    : isAnagram.py
"""

"""
1，两个字符串的元素根据索引映射到同一个表中
2，对于s或者t中的相同索引的元素x1，x2，x1和x2之前的非重复元素y1，y2的个数应该是相等的
3，两个字符串格式应该相同
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return all(s.index(s[i]) == t.index(t[i]) for i in range(len(s)))


if __name__ == '__main__':
    so = Solution()
    print(so.isIsomorphic("egg", "add"))
