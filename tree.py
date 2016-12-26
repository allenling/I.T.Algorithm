# coding=utf-8


class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.nums = 1
        self.left = left
        self.right = right


class BalancedBinaryTree(object):
    '''
    平衡二叉树
    节点的平衡因子是它的左子树的高度减去它的右子树的高度（有时相反）。带有平衡因子1、0或 -1的节点被认为是平衡的
    带有平衡因子 -2或2的节点被认为是不平衡的，并需要重新平衡这个树。平衡因子可以直接存储在每个节点中，或从可能存储在节点中的子树高度计算出来。
    http://www.cnblogs.com/vamei/archive/2013/03/21/2964092.html
    按照二叉搜索树的方式添加节点，然后判断是否出现了失衡的情况，若失衡，则各种旋转
    '''
    pass


def main():
    data = [23, 20, 62, 60, 59, 82, 17, 81, 27, 38]
    bbst = BalancedBinaryTree(data)
    bbst.print_graphic()
    print '-------initial------'
    bbst.insert(21)
    bbst.print_graphic()
    print '-----insert 21--------'
    bbst.delete(62)
    bbst.print_graphic()
    print '------deleet 62-------'


if __name__ == '__main__':
    main()
