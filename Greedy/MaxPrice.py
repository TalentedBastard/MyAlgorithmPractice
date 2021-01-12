"""
@Time    : 2021/1/11 23:00
@Author  : MD
@File    : MaxPrice.py
"""

"""
小偷能拿走多少东西，可以拿走东西的一部分，（商品单价，重量）
"""
goods = [(60, 10), (100, 20), (120, 30)]


def MaxPrice(goods, capacity):
    # goods按收益排序
    goods.sort(key=lambda x: x[0] / x[1],reverse=True)
    # 定义总价
    total = 0
    for i, (price, weight) in enumerate(goods):
        # 如果容量大于物品A的重量，可以放下全部A
        if capacity > weight:
            capacity -= weight
            total += price
        # 如果小于物品A的重量，只能放下一部分
        else:
            total += (capacity / weight) * price
    return total


if __name__ == '__main__':
    print(MaxPrice(goods, 60))
