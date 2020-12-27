"""
@Time    : 2020/12/27 15:51
@Author  : MD
@File    : bucket_sort.py
"""
"""
步骤：
    1，将数据根据数值大小填入不同分桶中
    2，确保桶内有序
    3，按顺序合并所有桶
时间复杂度：
    桶排序效率往往取决于数据分布，也就是桶划分的合理性，数据越分散，每个桶数据差不多，速度越快
    最坏: n*n*k
    平均：n+k
空间复杂度：nk
"""

def bucket_sort(l, max_num=1000,n=100):
    """
    在保证桶内有序时，新数比之前的数小就是从小到大排序，反之，从大到小
    :param l: 待排数组
    :param max: 待排数组最大值
    :param: 桶个数
    :return: 排好序的数组
    """
    buckets = [[] for _ in range(n)] # 创建桶，n个

    for var in l:
        i = min(var // (max_num // n), n-1) # 值应该放在哪个桶里
        buckets[i].append(var)

        for j in range(len(buckets[i])-1, 0, -1): # 保证桶内有序，利用冒泡排序思想
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j],buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break

    result = []
    for bucket in buckets:
        if len(bucket)>0:
            result += bucket
        else:
            continue
    return result

if __name__ == '__main__':
    import random
    l = [random.randint(0,100) for i in range(10)]
    print(l)
    random.shuffle(l)
    print(bucket_sort(l, max_num=100, n=10))

