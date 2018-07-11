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


def adjust_heap(root_index, data, size):
    while root_index < size:
        left_child_index = root_index * 2 + 1
        right_child_index = left_child_index + 1
        if left_child_index >= size:
            break
        max_child_value = data[left_child_index]
        max_child_index = left_child_index
        if right_child_index < size and data[right_child_index] > max_child_value:
            max_child_value = data[right_child_index]
            max_child_index = right_child_index
        if data[root_index] < max_child_value:
            data[root_index], data[max_child_index] = max_child_value, data[root_index]
            root_index = max_child_index
            continue
        break


def heap_sort(data):
    '''
    http://www.cnblogs.com/skywang12345/p/3602162.html
    http://bubkoo.com/2014/01/14/sort-algorithm/heap-sort/

    最大堆用来做升序的(从小到大)
    最小堆用来做降序的(大到小)
    这是因为第一次构建堆之后，会将最后一个元素和第一个元素进行互换，达到剔除第一个元素， 并且将最后一个元素加到第一个位置， 重新整理堆的效果
    所以，如果是最大堆，则第一个构建堆之后，第一个是最大值， 然后将第一个和最后一个元素互换，这个时候，最大值就是最后一个元素，然后将列表的大小
    缩小一个，这样，再次对列表进行堆整理的时候，就不会影响到最大元素，这样每次都是最大元素和第一个元素互换，所以较大的元素必定在后面，达到升序的效果

    关于top k问题
    http://blog.csdn.net/handsomekang/article/details/41346645
    '''
    size = len(data)
    root_index = int(size / 2 - 1)
    # 第一步, 建立大根堆, 注意这里是从size/2 - 1开始
    # 也就是经过第一步之后, 数组就是一个大根堆了, 也就是父节点都比
    # 其子节点大或等于, 其子节点也是一个大根堆
    while root_index >= 0:
        adjust_heap(root_index, data, size)
        root_index -= 1
    size -= 1
    # 经过第一步, 也就是建立大根堆之后, 我们得到的顶部元素就是最大值了
    # 下面是调整为有序数组
    # 顶部元素和最后一个元素(最后一个元素会变化)交换, 然后顶部元素会沉到合适的位置
    # 所以下面一步就是通过堆树的维护操作, 使得顶部元素永远是最大值
    # 那么我们每次都把顶部元素和最后一个元素交换, 这样我们第一次得到最大元素
    # 第二次我们得到第二大元素, 依以此类推
    while size:
        data[0], data[size] = data[size], data[0]
        adjust_heap(0, data, size)
        size -= 1


def binary_search(data, value):
    '''
    二分搜索
    二分搜索和二叉搜索树很类似, 只是二叉查找树不要求有序, 只要求左节点比其父节点小, 右节点比父节点大就好了
    '''
    NOT_FOUND = -1
    size = len(data)
    if size == 0:
        return NOT_FOUND
    if value > data[-1] or data[0] > value:
        return NOT_FOUND
    if value == data[-1]:
        return size - 1
    if value == data[0]:
        return 0
    if size == 2:
        return NOT_FOUND
    start, end = 0, size
    while start < end:
        if end - start == 1:
            if data[end] == value:
                return end
            elif data[start] == value:
                return start
            return NOT_FOUND
        middle = int((end - start) / 2) + start
        if value < data[middle]:
            end = middle
        elif value > data[middle]:
            start = middle
        else:
            return middle
    return NOT_FOUND


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


def pop_sort(data):
    '''
    https://blog.csdn.net/guoweimelon/article/details/50902597
    优化就是, 如果某一趟没有位置交换, 那么直接break就好了, 证明此时已经排序好了
    比如一个已经排序好的数组, 第一趟没有位置交换, 那么直接退出, 而一般的冒泡则是继续
    '''
    len_data = len(data)
    tail = len_data - 1
    while tail >= 1:
        for index, value in enumerate(data[:tail]):
            next_index = index + 1
            next_value = data[next_index]
            if next_value < value:
                data[next_index], data[index] = data[index], data[next_index]
        print(tail, data)
        tail -= 1
    return


def main():
    data = [3, 6, 4, 2, 11, 10, 5]
    pop_sort(data)
    print(data)

    print('--------pop_sort-----------\n')

    data = [3, 6, 4, 2, 11, 10, 5]
    insert_sort(data)
    print(data)

    print('--------insert_sort-----------\n')

#     data = [5, 8, 3, 2, 1]
#     shell_insert_sort(data)
#     print(data)
#     print('-------------------')

    data = [20, 30, 90, 40, 70, 110, 60, 10, 100, 50, 80]
    heap_sort(data)
    print(data)

    print('-------------heap_sort-------\n')

    tmp = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
    datas = [[tmp, tmp[i]] for i in range(0, len(tmp))]
    datas.append([[1, 5], 3])
    datas.append([[], 1])
    datas.append([list(range(100, 120)), 1])
    for data, value in datas:
        print(data, value, binary_search(data, value))

    print('-------------binary_search-------')


if __name__ == '__main__':
    main()
