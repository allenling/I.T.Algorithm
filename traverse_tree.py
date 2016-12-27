# coding=utf-8
from __future__ import unicode_literals
from __future__ import absolute_import
import tree_node


def depth_order(root):
    '''
    层序遍历
    每层有2**(n-1)个节点, 若所剩下的节点都是None, 就跳出
    '''
    res = []
    tmp = [root]
    d = 0
    while tmp:
        if not any(tmp):
            break
        depth_list = []
        count = 2**d
        while count:
            count -= 1
            node = tmp.pop(0)
            if not node:
                continue
            tmp.extend([node.left, node.right])
            depth_list.append(node.value)
        d += 1
        res.append(depth_list)
    return res


def depth_order_sec(root):
    '''
    层序遍历, 输出一维数组
    '''
    tmp = [root]
    res = []
    while tmp:
        node = tmp.pop(0)
        res.append(node.value)
        if node.left:
            tmp.append(node.left)
        if node.right:
            tmp.append(node.right)
    return res


def pre_order(root):
    '''
    前序遍历, 根节点->左子节点->右子节点
    '''
    tmp = [root]
    res = []
    while tmp:
        node = tmp.pop(0)
        if not node:
            continue
        tmp.insert(0, node.right)
        tmp.insert(0, node.left)
        res.append(node.value)
    return res


def middle_order(root):
    '''
    中序遍历, 左子节点->根节点->右子节点
    自己没思路, 下面抄别人的
    时间是O(n), 空间是O(log(n)), 这是因为我们寻找左边节点的时候, 一层一层往下找, 所以栈中最多的时候有log(n)个元素, log(n)也就是树高
    '''
    if root is None:
        return
    myStack = []
    node = root
    res = []
    while node or myStack:
        while node:
            # 从根节点开始，一直找它的左子树
            myStack.append(node)
            node = node.left
        # while结束表示当前节点node为空，即前一个节点没有左子树了
        node = myStack.pop()
        res.append(node.value)
        # 开始查看它的右子树
        node = node.right
    return res


def back_order(root):
    '''
    后序遍历, 左子节点->右子节点->根节点
    '''
    tmp = [root]
    res = []
    while tmp:
        node = tmp.pop(0)
        if not node:
            continue
        tmp.insert(0, node.left)
        tmp.insert(0, node.right)
        res.insert(0, node.value)
    return res


def main():
    data = ['a', 'b', 'c', 'd', None, 'e', 'f', None, None, None, None, 'g', 'h', None, 'i']
    root = tree_node.build_complete_binary_tree_from_array(data)
    print 'pre order %s' % pre_order(root)
    print 'middle order %s' % middle_order(root)
    print 'back order %s' % back_order(root)
    print 'depth order %s' % depth_order_sec(root)
    for d in depth_order(root):
        print ' '.join(d)

if __name__ == '__main__':
    main()
