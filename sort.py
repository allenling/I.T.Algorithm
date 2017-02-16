# coding=utf-8
from __future__ import unicode_literals
from __future__ import absolute_import
'''
+--------------+-----------+-----------+----------+------------+--------+--------+
|              +           +           +          +            +        +        +
| 排序方法      + 平均情况    + 最坏情况    + 最好情况   + 空间复杂度  + 稳定性   + 复杂性  +
|              +           +           +          +            +        +        +
+--------------+-----------+-----------+----------+------------+--------+--------+
|              +           +           +          +            +        +        +
| 直接插入排序   + O(n^2)    + O(n^2)    + O(n)     + O(1)       + 稳定    + 简单    +
|              +           +           +          +            +        +        +
+--------------+-----------+-----------+----------+------------+--------+--------+
|              +           +           +          +            +        +        +
| 希尔排序      + O(nlog2n) + O(nlog2n) +          + O(1)       + 不稳定   + 叫复杂  +
|              +           +           +          +            +        +        +
+--------------+-----------+-----------+----------+------------+--------+--------+
'''


def insert_sort(data):
    '''
    能保证前N个是有序的，所有当前的元素比它左边的大的时候，就没必要再循环下去了
    '''
    if not data or len(data) <= 1:
        return data
    for i in range(1, len(data)):
        j = i
        while j:
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
                j -= 1
                continue
            break


def shell_insert_sort(data):
    '''
    先取一个正整数 d1(d1 < n)，把全部记录分成 d1 个组，所有距离为 d1 的倍数的记录看成一组，然后在各组内进行插入排序
    然后取 d2(d2 < d1)
    重复上述分组和排序操作；直到取 di = 1(i >= 1) 位置，即所有记录成为一个组，最后对这个组进行插入排序。一般选 d1 约为 n/2，d2 为 d1 /2， d3 为 d2/2 ，…， di = 1。
    这里简单的d1=N/2, d2=d1/2,...
    '''
    if not data or len(data) <= 1:
        return data
    vector = len(data) / 2
    while vector > 0:
        tmp = 0
        while tmp < vector:
            tmp_data = data[tmp::vector]
            insert_sort(tmp_data)
            data[tmp::vector] = tmp_data
            tmp += 1
        vector = vector / 2


def merge(data1, data2):
    tmp = []
    p1 = p2 = 0
    size1 = len(data1)
    size2 = len(data2)
    while p1 < size1 and p2 < size2:
        if data1[p1] <= data2[p2]:
            tmp.append(data1[p1])
            p1 += 1
            continue
        tmp.append(data2[p2])
        p2 += 1
    if p1 == size1:
        tmp.extend(data2[p2:])
    else:
        tmp.extend(data1[p1:])
    return tmp


def merge_sort(data):
    '''
    归并排序
    分治策略, 复杂度都是O(nlog2(n)), 空间是O(n), 稳定
    一般递归实现
    个人不喜欢递归, 所以尽量非递归
    '''
    while True:
        first = data.pop(0)
        second = data.pop(0)
        first = [first] if not isinstance(first, list) else first
        second = [second] if not isinstance(second, list) else second
        tmp = merge(first, second)
        if not data:
            data = tmp
            break
        data.append(tmp)
    return data


def adjust_heap(root, data, size):
    while root < size:
        child = root * 2 + 1
        if child >= size:
            break
        if child + 1 < size and data[child] < data[child + 1]:
            child += 1
        if data[root] < data[child]:
            data[root], data[child] = data[child], data[root]
            root = child
            continue
        break


def heap_sort(data):
    '''
    最大堆用来做升序的(从小到大)
    最小堆用来做降序的(大到小)
    这是因为第一次构建堆之后，会将最后一个元素和第一个元素进行互换，达到剔除第一个元素， 并且将最后一个元素加到第一个位置， 重新整理堆的效果
    所以，如果是最大堆，则第一个构建堆之后，第一个是最大值， 然后将第一个和最后一个元素互换，这个时候，最大值就是最后一个元素，然后将列表的大小
    缩小一个，这样，再次对列表进行堆整理的时候，就不会影响到最大元素，这样每次都是最大元素和第一个元素互换，所以较大的元素必定在后面，达到升序的效果

    关于top k问题
    http://blog.csdn.net/handsomekang/article/details/41346645
    '''
    size = len(data)
    root = size / 2 - 1
    while root >= 0:
        adjust_heap(root, data, size)
        root -= 1
    size -= 1
    while size:
        data[0], data[size] = data[size], data[0]
        adjust_heap(0, data, size)
        size -= 1


def binary_search(data, value):
    '''
    二分搜索
    二分搜索和二叉搜索树很类似, 只是二叉查找树不要求有序, 只要求左节点比其父节点小, 右节点比父节点大就好了
    '''
    if value > data[-1] or data[0] > value:
        return -1
    size = len(data)
    if value == data[-1]:
        return size - 1
    if value == data[0]:
        return 0
    start, end = 0, size
    while start < end:
        middle = ((end - start) / 2) + start
        if value < data[middle]:
            end = middle - 1
        elif value > data[middle]:
            start = middle + 1
        else:
            return middle
    return -1


def adjust_middle(data, start, end):
    point_index, point = start, data[start]
    while start < end:
        while data[end] >= point and start < end:
            end -= 1
        data[end], data[point_index] = data[point_index], data[end]
        point_index = end
        while data[start] <= point and start < end:
            start += 1
        data[start], data[point_index] = data[point_index], data[start]
        point_index = start
    return start


def quick_sort(data, start, end):
    '''
    快排
    分治策略
    最坏O(n**2), 最好和平均都是O(nlog2(n)), 空间O(nlog2(n)), 不稳定
    没想出非递归方案
    '''
    if start < end:
        middle = adjust_middle(data, start, end)
        quick_sort(data, start, middle - 1)
        quick_sort(data, middle + 1, end)


def main():
    data = [5, 8, 3, 2, 1]
    insert_sort(data)
    print data

    data = [5, 8, 3, 2, 1]
    shell_insert_sort(data)
    print data

    data = [3, 1, 5, 7, 2, 4, 9, 6, 10, 8]
    heap_sort(data)
    print data
    print binary_search([1, 5], 3)

if __name__ == '__main__':
    main()
