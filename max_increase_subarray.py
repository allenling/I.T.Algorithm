# coding=utf-8
'''
最长递增子序列
给定一个长度为N的数组，找出一个最长的单调自增子序列（不一定连续，但是顺序不能乱）
例如：给定一个长度为6的数组A{5， 6， 7， 1， 2， 8}，则其最长的单调递增子序列为{5，6，7，8}，长度为4.

有数组A，前m个元素的最大子数组的长度是n，有下面记录数组B, B中是记录长度为n的时候，下标最大的数值, 长度为n

B = {.., a, b, c}
对于下一个元素d

1. 若d > c, 则很显然，对于A，abcd是递增的, 所以前面m+1个元素的最长递增子数组的长度就是n + 1

2. 若d < c, 则长度为m+1的时候，最长递增子数组的长度不可能大于n,因为c>d, 所以可能是n, n-1, n-2, n-3...，下面是例子

  2.1. 若d > d, A和B当前都是10, 20, 30, A的下一个元素是25, 则很明显长度为3的最大下标的数值就是25， 所以B就变为10,20,25
  2.2 若d > a, A和B当前都是10, 20, 30, A的下一个元素是15, 则很明显长度为2的最大下标的数值就是15， 所以B就变为10,15,30

依次类推，则只需要二分找到比d大的最小值，替换掉就好

'''


def binary_search(data, v):
    start, end = 0, len(data) - 1
    mid = 0
    while start < end:
        if end - start == 1:
            mid = end
            break
        mid = (end - start) / 2 + start
        if data[mid] < v:
            start = mid
        else:
            end = mid
    return mid


def mis(data):
    b = [data[0]]
    for d in data[1:]:
        if d > b[-1]:
            b.append(d)
            continue
        index = binary_search(b, d)
        b[index] = d
    return len(b)


def main():
    d = [2 , 1 , 5 , 3 , 6,  4,  8,  9,  7]
    print mis(d)

if __name__ == '__main__':
    main()
