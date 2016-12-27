# coding=utf-8
from __future__ import unicode_literals
from __future__ import absolute_import
from tree_node import Node


class BinarySearchTree(object):
    '''
    二叉搜索树
    '''

    def __init__(self, data):
        self.root = None
        for v in data:
            self.insert(v)

    def search(self, v):
        parent = None
        node = self.root
        tmp = [self.root]
        while tmp:
            n = tmp.pop(0)
            if not n:
                break
            if n.value > v:
                parent = n
                node = n.left
                tmp.append(n.left)
            elif n.value < v:
                parent = n
                node = n.right
                tmp.append(n.right)
        return parent, node

    def insert_node_from_parent(self, node, parent=None):
        if not node:
            return
        if not self.root:
            self.root = node
            return
        tmp = [parent] if parent else [self.root]
        v = node.value
        proot = parent
        while tmp:
            n = tmp.pop(0)
            if n.value > v:
                if not n.left:
                    proot.left = node
                    return
                tmp.append(n.left)
            elif n.value < v:
                if not n.right:
                    proot.right = node
                    return
                tmp.append(n.right)

    def insert(self, v):
        parent, node = self.search(v)
        if node:
            node.nums += 1
            return
        new_node = Node(v)
        self.insert_node_from_parent(new_node, parent)

    def get_node_down_max(self, node):
        parent = None
        max_node = node
        if not node:
            return parent, max_node
        tmp = [node.right]
        while tmp:
            n = tmp.pop(0)
            if not n:
                break
            parent = max_node
            max_node = n
            tmp.append(n.right)
        return parent, max_node

    def delete(self, v):
        parent, node = self.search(v)
        if not node:
            return
        if node.nums > 1:
            node.nums -= 1
            return
        if parent and parent.left and parent.left.value == node.value:
            parent.left = None
        elif parent and parent.right and parent.right.value == node.value:
            parent.right = None
        else:
            self.root = None
        lchild = node.left
        rchild = node.right
        new_parent, new_node = self.get_node_down_max(lchild)
        if new_node is None:
            self.insert_node_from_parent(rchild, parent)
            return
        if new_parent:
            new_parent.right = new_node.left
        self.insert_node_from_parent(new_node, parent)
        new_node.left = lchild
        new_node.right = rchild

    def print_graphic(self):
        ns = [self.root]
        while ns:
            node = ns.pop(0)
            if not node:
                continue
            print node.left.value if node.left else None, node.value, node.right.value if node.right else None
            ns.extend([node.left, node.right])


def main():
    data = [70, 40, 51, 31, 30, 80, 50, 59, 39]
    bst = BinarySearchTree(data)
    bst.print_graphic()
    print '--------------'
    print bst.search(30), bst.search(31)
    bst.delete(40)
    print bst.search(40)
    bst.print_graphic()
    print '--------------'
    bst.delete(70)
    bst.print_graphic()
    print '------delete root--------'

if __name__ == '__main__':
    main()
