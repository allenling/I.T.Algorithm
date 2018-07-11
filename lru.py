'''
Created on Jul 11, 2018

@author: allenling

http://www.cnblogs.com/dolphin0520/p/3741519.html
'''


class ListNode:

    def __init__(self, key=None, prev_node=None, next_node=None):
        self.prev_node = prev_node
        self.key = key
        self.next_node = next_node
        return

    def __str__(self):
        return 'Node:' + str(self.key)

    def __repr__(self):
        return self.__str__()


class LRU:

    def __init__(self, max_len=-1):
        self.header = ListNode()
        self.tailer = None
        self.data = {}
        self.max_len = max_len
        self.current_size = 0
        return

    def get(self, key):
        value = self.data.get(key, None)
        if value is None:
            return -1
        self.adjust_data(key)
        return value.value

    def set(self, key, value):
        old_value = self.data.get(key, None)
        if old_value is None and self.current_size == self.max_len:
            self._delete()
        self.current_size += 1
        if old_value is None:
            self.data[key] = {'value': value, 'listnode': ListNode(key=key)}
        else:
            old_value['value'] = value
        self.adjust_data(key)
        return

    def adjust_data(self, key):
        key_node = self.data[key]['listnode']

        header_next_node = self.header.next_node

        if header_next_node is key_node:
            return

        prev_key_node = key_node.prev_node
        next_key_node = key_node.next_node

        if prev_key_node is None and next_key_node is None:
            self.header.next_node = key_node
        else:
            prev_key_node.next_node = next_key_node
            key_node.prev_node = None
            if next_key_node is not None:
                next_key_node.prev_node = prev_key_node
            key_node.next_node = None

        key_node.prev_node = self.header
        key_node.next_node = header_next_node

        if header_next_node is not None:
            header_next_node.prev_node = key_node
        else:
            self.tailer = key_node
        return

    def _delete(self):
        assert self.current_size == self.max_len
        assert self.tailer is not None

        tailer_key = self.tailer.key

        tailer_prev_node = self.tailer.prev_node
        tailer_prev_node.next_node = None

        self.tailer.prev_node = None

        self.tailer = None
        del self.data[tailer_key]
        self.current_size -= 1
        if self.current_size == 0:
            self.tailer = None
        else:
            self.tailer = tailer_prev_node
        return


lru = LRU(max_len=3)

for i in range(10):
    print(i)
    lru.set(i, i)
    print(lru.data, lru.current_size, lru.tailer)

    node = lru.header

    while node is not None:
        print(node, node.prev_node, node.next_node)
        node = node.next_node

    print('-------------------------')
