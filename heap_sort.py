"""
@Time    : 2020/12/26 12:25
@Author  : MD
@File    : heap_sort.py
"""


"""
堆排序分为三部分：
    1，构建堆
    2，堆内调整
    3，依次返回堆顶元素
    
时间复杂度：
    建堆：n
    堆排序：nlog(n)
空间复杂度：1
"""

def sift(l,low,high):
    """
    大根堆堆内调整代码，小根堆类似，只需要找到左右孩子最小即可
    步骤：
        1，初始化i=根节点下标，j=i所在节点的lchild
        2，开始循环，结束条件为i所在节点的rchild 不越界(<high)
        3, 找出lchild和rchild更大的，与i换位置
        4，更新i，j，i下移一层，j变成新lchild
        5，循环结束，tmp回到正确位置
    :param l: 待排序数组
    :param low: 根节点下标，是下标最小值
    :param high: 堆底最后一个叶子结点下标，是下标最大值
    :return: None，执行此方法完成一个有序堆
    """
    i = low # i是最顶端下标
    j = i*2+1   # j是当前节点左孩子（初始化时为根节点）
    tmp = l[i] # 堆顶元素
    while j <= high:    # 保证孩子节点有数
        if j+1 <= high and l[j+1] > l[j]: # 找到左右孩子中最大的一个，且保证不越界
            j = j+1
        if l[j] > tmp: # 找到比当前元素小的，进行转换，数换完之后，i和j进行更新，i到了j的位置，j指向新i的孩子节点
            l[i] = l[j]
            i = j
            j = i*2+1
        else:
            break
    l[i] = tmp # 最后没有找到比当前元素更小的，或者没有孩子节点了，跳出循环，i到了应该在的位置，tmp的值放回i


def heap_sort(l):
    """
    堆排序主方法分为两步：
        1，建堆
        2，排序
    :param l: 待排序的数组
    :return:
    """
    # 建堆
    n = len(l)
    for i in range((n-2)//2, -1, -1):    # 建堆过程是自底向上，保证节点内有序，最终保证全堆有序
        sift(l, i, n-1)

    # 排序
    for i in range(n-1, -1, -1):
        l[0], l[i] = l[i], l[0]
        sift(l, 0, i-1) # i-1是新的high

if __name__ == '__main__':
    import random
    l = [i for i in range(10)]
    random.shuffle(l)
    print("初始的l：    %s" % l)
    heap_sort(l)
    print("堆排序后的l： %s" % l)
