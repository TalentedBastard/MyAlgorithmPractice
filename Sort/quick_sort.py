"""
@Time    : 2021/7/15 15:08
@Author  : MD
@File    : quick_sort.py
@Software: PyCharm
"""

"""
步骤：
    1，if判断参数，不对直接return
    2，找到分割值x，x左边都小于它，右边都大于它
    3，递归整个列表
"""


class quick_sort(object):
    def __init__(self):
        pass

    def __swap(self, data, lo, hi):
        data[lo], data[hi] = data[hi], data[lo]

    def __sort(self, data, l, r):
        if l >= r:
            return
        base = self.__cut(data, l, r)
        self.__sort(data, l, base - 1)
        self.__sort(data, base + 1, r)

    def __cut(self, data, l, r):
        lo, hi = l, r
        base = data[l]
        while True:
            lo += 1
            # 从左往右找到大于基准值的
            while data[lo] < base:
                if lo == r:
                    break
                lo += 1
            # 从右往左找到小于基准值的
            while data[hi] > base:
                if hi == l:
                    break
                hi -= 1

            if lo > hi:
                break
            # 不满足两个条件的进行交换，此时是两指针的元素进行交换
            self.__swap(data, lo, hi)
        # 最后是起始元素换到分割点，相当于插入指定位置
        self.__swap(data, l, hi)
        return hi

    def sort(self, data):
        return self.__sort(data, 0, len(data) - 1)


if __name__ == '__main__':
    data = [5,4,1,9,]
    print(data)
    qs = quick_sort()
    qs.sort(data)
    print(data)
