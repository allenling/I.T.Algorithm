'''
Created on Jul 11, 2018

@author: allenling

https://www.cnblogs.com/dolphin0520/p/3749259.html

为了能够淘汰最少使用的数据，因此LFU算法最简单的一种设计思路就是 利用一个数组存储 数据项，用hashmap存储每个数据项在数组中对应的位置
然后为每个数据项设计一个访问频次，当数据项被命中时，访问频次自增，在淘汰的时候淘汰访问频次最少的数据。这样一来的话，在插入数据和访问数据的时候都能达到O(1)的时间复杂度
在淘汰数据的时候，通过选择算法得到应该淘汰的数据项在数组中的索引，并将该索引位置的内容替换为新来的数据内容即可，这样的话，淘汰数据的操作时间复杂度为O(n)。

另外还有一种实现思路就是利用 小顶堆+hashmap，小顶堆插入、删除操作都能达到O(logn)时间复杂度，因此效率相比第一种实现方法更加高效。
'''


class LittleHeap:
    '''
    小顶堆
    '''
    def __init__(self, max_len):
        self.max_len = max_len
        if max_len <= 0:
            self.delete = self._no_delete
            self.add = self._no_add
        else:
            self.delete = self._delete
            self.add = self._add
        self.data = []
        return

    def _no_delete(self):
        return

    def _no_add(self):
        return

    def _delete(self):
        return

    def _add(self):
        return


class LFU:

    def __init__(self, max_len=-1):
        self.heap = LittleHeap(max_len)
        return

    def get(self, key):
        return

    def set(self, key, value):
        return

    def _delete(self):
        self.heap.delete()
        return
