# coding=utf-8
'''
霍夫曼树
使用变长码来压缩要传输的数据, 压缩性能最好
权路径长度WPL最小的二叉树称为赫夫曼树或最优二叉树。
'''


class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.nums = 1
        self.left = left
        self.right = right
        self.path = ''

    def __repr__(self):
        return '%s:%s' % (self.value, self.path)

    def __str__(self):
        return self.__repr__()


class HuffmanTree(object):

    def __init__(self, data):
        first = min(data)
        data.pop(data.index(first))
        sec = min(data)
        data.pop(data.index(sec))
        node = Node(first + sec)
        if first > sec:
            node.left = Node(sec)
            node.right = Node(first)
        else:
            node.left = Node(first)
            node.right = Node(sec)
        node.left.path = '0'
        node.right.path = '1'
        while data:
            minv = min(data)
            data.pop(data.index(minv))
            new_node = Node(minv + node.value)
            if minv > node.value:
                new_node.left = node
                new_node.right = Node(minv)
            else:
                new_node.left = Node(minv)
                new_node.right = node
            new_node.left.path = '0'
            new_node.right.path = '1'
            node = new_node
        self.root = node
        return

    def print_graphic(self):
        tmp = [self.root]
        while tmp:
            node = tmp.pop(0)
            if not node:
                continue
            tmp.extend([node.left, node.right])
            print node

    def print_code(self):
        res = []
        path = [str(self.root.path)]
        ps = [self.root, self.root]
        tmp = [self.root.left, self.root.right]
        while tmp:
            node = tmp.pop(0)
            path.append(node.path)
            if not node.left and not node.right:
                p = ''.join(path)
                res.append([node.value, p])
                path.pop()
                cp = ps.pop(0)
                if cp.value != ps[0].value:
                    path.pop()
                continue
            if node.right:
                ps.insert(0, node)
                tmp.insert(0, node.right)
            if node.left:
                ps.insert(0, node)
                tmp.insert(0, node.left)
        return res


def main():
    data = [43, 14, 29, 14]
    ht = HuffmanTree(data)
    ht.print_graphic()
    print '-----print graphic--------'
    for c in ht.print_code():
        print c
    print '-----print code--------'

if __name__ == '__main__':
    main()
