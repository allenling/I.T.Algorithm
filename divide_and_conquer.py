# coding=utf-8
'''
算法导论： 分治策略
'''


def find_max_cross_subarray(data, start, mid, end):
    left_index = mid
    right_index = mid + 1
    left_max_sum = None
    tmp_sum = 0
    while left_index >= start:
        tmp_sum += sum(data[left_index: mid + 1])
        if tmp_sum > left_max_sum:
            left_max_sum = tmp_sum
            max_start = left_index
        left_index -= 1
    right_max_sum = None
    tmp_sum = 0
    while right_index <= end:
        tmp_sum += sum(data[right_index:right_index + 1])
        if tmp_sum > right_max_sum:
            right_max_sum = tmp_sum
            max_end = right_index
        right_index += 1
    return max_start, max_end, right_max_sum + left_max_sum


def recursion_for_max_sum_of_subarray(data, start, end):
    '''
    分治策略求和最大的连续子数组
    '''
    if start == end:
        return data[start], start, end
    mid = start + ((end - start) / 2)
    left_start, left_end, left_max = recursion_for_max_sum_of_subarray(data, start, mid)
    right_start, right_end, right_max = recursion_for_max_sum_of_subarray(data, mid + 1, end)
    cross_start, cross_end, cross_max = find_max_cross_subarray(data, start, mid, end)
    if left_max > right_max and left_max > cross_max:
        return left_start, left_end, left_max
    if right_max > left_max and right_max > cross_max:
        return right_start, right_end, right_max
    return cross_start, cross_end, cross_max


def max_sum_of_subarray(data):
    '''
    线性时间求和最大的连续子数组
    假设data[i:j]是data[i:j]的最大连续子数组，则若data[j+1]是负数，则直接忽略，然后下一步
    若data[j+1]是正数，则求出data[p:j+1], pi<=p<=j+1，每一个的和和data[i:j]比较，所以
    最坏情形是: 都是正数， 则每一次都要计算data[p:j+1]的和，所以最坏情形下有2+3+4+5+...+n=(n+2)*(n/2)=O(n^2)
    最好的情形是第一个元素之后都是负数， 这样每一次我们都不需要计算data[p:j+1], 直接下一步就可以了，所以是O(n)
    但是，我们可以通过一个O(1)的比较方法求出data[i:j]和data[j+1]中的最大子数组, 所以就是O(1)0(n)=O(n)
    https://3meng.github.io/2016/02/08/Algorithm-of-Finding-Maximum-SubArray/
    '''
    start = end = 0
    current_sum = max_sum = data[0]
    size = len(data)
    i = 1
    first_p_index = None
    while i < size:
        current_sum += data[i]
        if data[i] < 0:
            i += 1
            continue
        if first_p_index:
            if current_sum > max_sum and current_sum > data[i]:
                end = i
                max_sum = current_sum
            elif data[i] > current_sum and data[i] > max_sum:
                start = end = i
                max_sum = data[i]
            pvalue = sum(data[first_p_index: i + 1])
            if pvalue > max_sum:
                max_sum = pvalue
                current_sum = max_sum
                start, end = first_p_index, i
                first_p_index = None
        else:
            if current_sum > max_sum and current_sum > data[i]:
                end = i
                max_sum = current_sum
            elif data[i] > current_sum and data[i] > max_sum:
                start = end = i
                current_sum = max_sum = data[i]
            else:
                first_p_index = i
        i += 1
    return start, end, max_sum


def main():
    dataset = [[13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7],
               [18, 20],
               [-2, -2, -3],
               [18, 20, -1],
               [18, 20, -77, 5, 40],
               [10, -11, 12]
               ]
    for data in dataset:
        print data, max_sum_of_subarray(data)
    print '------------'
    for data in dataset:
        print data, recursion_for_max_sum_of_subarray(data, 0, len(data) - 1)


if __name__ == '__main__':
    main()
