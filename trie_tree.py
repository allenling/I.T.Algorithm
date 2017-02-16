# coding=utf-8
'''
字典树
http://www.cnblogs.com/huangxincheng/archive/2012/11/25/2788268.html
'''
from sort import heap_sort


class Node(object):

    def __init__(self, value):
        self.value = value
        self.nums = 1
        self.childs = []

    def insert(self, s):
        ch = self.get_child(s)
        if not ch:
            ch = Node(s)
            self.childs.append(ch)
        return ch

    def get_child(self, s):
        for ch in self.childs:
            if ch.value == s:
                return ch
        return

    def __repr__(self):
        return '%s:%s' % (self.value, [_.value for _ in self.childs] if self.childs else [])

    def __str__(self):
        return self.__repr__()


class TrieTree(object):

    def __init__(self, data):
        self.root = Node(None)
        for d in data:
            self.insert(d)

    def get_prefix(self, s, index=1):
        while index <= len(s):
            yield s[0:index], index
            index += 1

    def insert(self, s):
        parent, node, prefix, pre_index = self.search(s)
        if not node:
            for prefix, pre_index in self.get_prefix(s, pre_index):
                parent = parent.insert(prefix)
            return
        node.nums += 1
        return

    def get(self, s):
        node = self.search(s)[1]
        if not node:
            return False
        return True

    def search(self, s):
        parent = self.root
        next_child = None
        tmp = [parent]
        for prefix, pre_index in self.get_prefix(s):
            node = tmp.pop(0)
            next_child = node.get_child(prefix)
            if not next_child:
                break
            parent = next_child
            tmp.append(next_child)
        return parent, next_child, prefix, pre_index

    def print_graphic(self):
        tmp = [self.root]
        while tmp:
            node = tmp.pop(0)
            if not node.childs:
                continue
            print node.value, [_.value for _ in node.childs]
            tmp.extend(node.childs)

    def print_order(self):
        tmp = [self.root]
        res = []
        while tmp:
            node = tmp.pop(0)
            if not node.childs:
                res.append((node.value, node.nums))
                continue
            new_child = sorted(node.childs, key=lambda x: x.value)
            while new_child:
                tmp.insert(0, new_child.pop())
        return res


def main():
    data = ['ab', 'ac', 'aac', 'ef', 'cc', 'cks', 'ca', 'asd', 'efjs', 'ejs', 'ab']
    trie = TrieTree(data)
    trie.print_graphic()
    print '---------initial---------'
    ts = ['ab', 'ac', 'ba', 'efjs']
    for t in ts:
        print '%s: %s' % (t, trie.get(t))
    print '---------search---------'
    print trie.print_order()
    print '---------print order---------'
    heap_sort(data)
    print data
    print '---------heap sort---------'

if __name__ == '__main__':
    main()
