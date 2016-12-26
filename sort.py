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

if __name__ == '__main__':
    main()
