"""
@Time    : 2021/1/9 10:14
@Author  : MD
@File    : groupThePeople.py
"""
import collections

"""
给groupsizes里的人分组，相同序号放在一个组
"""
class Solution:
    def groupThePeople(self, groupSizes):
        groups = collections.defaultdict(list)
        for i, j in enumerate(groupSizes):
            groups[j].append(i)

        res = []
        for gsize,users in groups.items():
            for i in range(0, len(users), gsize):
                res.append(users[i:i+gsize])
        return res



if __name__ == '__main__':
    groupSizes = [3,3,3,3,3,1,3]
    so = Solution()
    print(so.groupThePeople(groupSizes))
