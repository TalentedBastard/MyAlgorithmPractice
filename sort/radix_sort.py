"""
@Time    : 2020/12/27 16:38
@Author  : MD
@File    : radix_sort.py
"""
"""
基数排序
步骤：
    1，将数组按最高位分桶，分到10个桶里
    2，将桶里所有数排成新数组
    3，重复1，2，最后个位完成分桶排序，整体数组有序
时间：kn  k=lgN N=数值大小    数组中元素数值比较小时，基数排序比快排还要快，随着数值增大，基数排序变慢
空间：
"""

def radix_sort(l):
    """
    基数排序
    :param l: 待排数组
    :return: 排序完成数组
    """
    from math import log
    its = int(log(max(l), 10))     # log函数取到最高位
    for it in range(its+1):
        buckets = [[] for _ in range(10)]
        for val in l:
            i = (val // 10 ** it) % 10
            buckets[i].append(val)

        l.clear()

        for bucket in buckets:
            l.extend(bucket)

    return l

if __name__ == '__main__':
    import random
    l = [random.randint(0,100) for i in range(10)]
    print(l)
    random.shuffle(l)
    print(radix_sort(l))