"""
@Time    : 2020/12/26 15:02
@Author  : MD
@File    : merge_sort.py
"""


def merge(l, low, mid, high):
    """
    将局部有序变成全局有序
    :param l: 数组
    :param low: 初始下标
    :param mid: 中间下标
    :param high: 结尾下标
    :return: 全局有序的数组
    """
    # mid = (low + high) // 2
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if l[i] < l[j]:
            tmp.append(l[i])
            i += 1
        else:
            tmp.append(l[j])
            j += 1
    while i <= mid:
        tmp.append(l[i])
        i += 1
    while j <= high:
        tmp.append(l[j])
        j += 1
    l[low:high+1] = tmp

def merge_sort(l, low, high):
    """
    归并排序
    :param l: 数组
    :return: 排好序的数组
    """
    if low < high: # 局部有两个元素，进行递归
        mid = (low+high) // 2
        merge_sort(l,low,mid)
        merge_sort(l,mid+1,high)
        merge(l,low, mid, high)
    return l

if __name__ == '__main__':
    l = [2, 4, 5, 7, 1, 3, 6, 8]
    print(merge_sort(l, 0, 7))
