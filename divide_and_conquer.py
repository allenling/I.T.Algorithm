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
    return right_max_sum + left_max_sum, max_start, max_end


def recursion_for_max_sum_of_subarray(data, start, end):
    '''
    分治策略求和最大的连续子数组
    '''
    if start == end:
        return data[start], start, end
    mid = start + ((end - start) / 2)
    left_max, left_start, left_end = recursion_for_max_sum_of_subarray(data, start, mid)
    right_max, right_start, right_end = recursion_for_max_sum_of_subarray(data, mid + 1, end)
    cross_max, cross_start, cross_end = find_max_cross_subarray(data, start, mid, end)
    if left_max > right_max and left_max > cross_max:
        return left_max, left_start, left_end
    if right_max > left_max and right_max > cross_max:
        return right_max, right_start, right_end
    return cross_max, cross_start, cross_end


def max_sum_of_subarray(data):
    '''
    线性时间求和最大的连续子数组
    假设data[i:j]是data[i:j]的最大连续子数组，则若data[j+1]是负数，则直接忽略，然后下一步
    若data[j+1]是正数，则求出data[p:j+1], pi<=p<=j+1，每一个的和和data[i:j]比较，所以
    最坏情形是: 都是正数， 则每一次都要计算data[p:j+1]的和，所以最坏情形下有2+3+4+5+...+n=(n+2)*(n/2)=O(n^2)
    最好的情形是第一个元素之后都是负数， 这样每一次我们都不需要计算data[p:j+1], 直接下一步就可以了，所以是O(n)
    但是，我们可以通过一个O(1)的比较方法求出data[i:j]和data[j+1]中的最大子数组, 所以就是O(1)0(n)=O(n)
    '''
    max_sum, start, end = data[0], 0, 0
    end_point = 1
    size = len(data)
    tmp_sum = max_sum
    pindex, pvalue = -1, 0
    while end_point < size:
        tmp_sum += data[end_point]
        if pindex > -1:
            pvalue += data[end_point]
        if data[end_point] < 0:
            end_point += 1
            continue
        after_value = pvalue if pindex > -1 else data[end_point]
        if after_value > tmp_sum and after_value > max_sum:
            max_sum, start, end = after_value, pindex if pindex > -1 else end_point, end_point
            tmp_sum = after_value
            pindex, pvalue = -1, 0
        elif tmp_sum > after_value and tmp_sum > max_sum:
            pindex, pvalue = -1, 0
            max_sum, end = tmp_sum, end_point
        else:
            if pindex == -1:
                pindex = end_point
                pvalue = data[end_point]
        end_point += 1
    return max_sum, start, end


def main():
    data = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print recursion_for_max_sum_of_subarray(data, 0, len(data) - 1)
    print max_sum_of_subarray(data)


if __name__ == '__main__':
    main()
