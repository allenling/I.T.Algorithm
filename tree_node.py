# coding=utf-8
from __future__ import unicode_literals
from __future__ import absolute_import
import copy


class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.nums = 1
        self.left = left
        self.right = right

    def __str__(self):
        return 'Node(%s, %s, %s)' % (None if not self.left else self.left.value, self.value, None if not self.right else self.right.value)

    def __repr__(self):
        return self.__str__()


def build_complete_binary_tree_from_array(data):
    '''
    数组是完全二叉树的形式, 叶节点的子节点用None来代替
    '''
    tmp = copy.copy(data)
    root = Node(tmp.pop(0))
    nodes = [root]
    while tmp:
        node_tmp = []
        while nodes:
            node = nodes.pop(0)
            lv = tmp.pop(0)
            rv = tmp.pop(0)
            if not node or (lv is None and rv is None):
                continue
            lnode = Node(lv) if lv else None
            rnode = Node(rv) if rv else None
            node.left = lnode
            node.right = rnode
            node_tmp.append(lnode)
            node_tmp.append(rnode)
        nodes.extend(node_tmp)
    return root


def main():
    data = ['a', 'b', 'c', 'd', None, 'e', 'f', None, None, None, None, 'g', 'h', None, 'i']
    root = build_complete_binary_tree_from_array(data)
    print root

if __name__ == '__main__':
    main()
