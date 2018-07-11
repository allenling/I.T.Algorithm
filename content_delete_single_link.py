'''
Created on Jul 11, 2018

@author: allenling

O(1)删除单链表

思路是把要删除节点的下一个节点的值赋值到当前要删除的节点, 然后删除掉下一个节点

1 -> 2 -> 3

删除2, node=2, next_node = 3, node=3, delete next_node

注意:

1. 如果链表只有一个结点
2. 如果链表有多个结点，且删除最后一个结点，那么只能遍历链表

所以我们要传入header/root

http://www.cnblogs.com/xwdreamer/archive/2012/04/26/2472102.html
'''


class SignleLinked:

    def __init__(self, value):
        self.value = value
        self.next_node = None
        return


def get_prev_node(root, current_value):
    node = root
    res = None
    while True:
        if node.next_node.value == current_value:
            res = node
            break
        node = node.next_node
    return res


def delete_node(root, node):
    next_node = node.next_node
    if next_node is not None:
        node.value = next_node.value
        node.next_node = next_node.next_node
    elif root.next_node is node:
        root.next_node = node = None
    else:
        # 最后只能遍历链表, 找到前一个节点
        prev_node = get_prev_node(root, node.value)
        prev_node.next_node = next_node
        node = None
    return


def print_node_list(root):
    res = []
    node = root.next_node
    while node is not None:
        res.append(node.value)
        node = node.next_node
    print(res)
    return


def main():
    data = {}
    prev = root = SignleLinked(None)
    for i in range(10):
        tmp = SignleLinked(i)
        data[i] = tmp
        prev.next_node = tmp
        prev = tmp
    print_node_list(root)
    print('=============')
    for i in [0, 4, 9]:
        delete_node(root, data[i])
        print_node_list(root)
        print('-----------------')
    return


if __name__ == '__main__':
    main()
