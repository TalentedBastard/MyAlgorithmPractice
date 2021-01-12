"""
@Time    : 2021/1/11 22:43
@Author  : MD
@File    : Money.py
"""

"""
找零钱问题，贪心算法，先找最大面值，找不开之后找小一档面值，以此类推
"""
denomination = [100, 50, 20, 10, 1]


def GreedyMoney(denomination, money):
    res = [0 for _ in range(len(denomination))]
    for i, m in enumerate(denomination):
        res[i] = money // m
        money = money % m

    return res


if __name__ == '__main__':
    print(GreedyMoney(denomination, 386))
