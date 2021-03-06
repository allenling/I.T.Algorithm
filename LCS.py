# coding=utf-8
'''
动态规划解题最大子序列，其不要求连续，只要保证相对顺序就好, 如g,a,t,c和g,b,t,c的最大子序列就是g,t,c，而最大子字符串就是要求是连续的，所以就是t,c

1.
序列a: a1,a2,a3,...,am
序列b: b1,b2,b3,...,bn
两者的其中一个最大子序列c: c1,c2,c3,...,cp
实际例子: a: g,a,t,c, b: g, b, t, t

然后我们计算a中每一个子序列和b中每一个子序列的长度，最大值就是结果，

情况1: ai,...aj和bk,...,bl比较，如果aj==bl，则很显然，最大子序列的长度就是ai,...,aj-1和bk,...,bl-1的长度加1

情况2: 若不相等，则是ai,..,aj-1和bk,...,bl的最长公共子序列长度和ai,..,aj和bk,...,bl-1的最长公共子序列长度的最大值.

如: g,a和g,b, a不等于b, 所以序列g,a和g,b的最长公共子序列的长度要是是g和g,b两者的最长公共子序列，或者是g,a和g的最长公共子序列的长度.

用一个二维矩阵记录每一个子问题的结果，然后直接用.

    g a t c
  0 0 0 0 0
g 0 0 0 0 0
b 0 0 0 0 0
t 0 0 0 0 0
t 0 0 0 0 0

当g==g的时候，其单元格的值就是其对角线的值加1，对角线就是情况1
当a!=b的时候，其单元格的值就是其上一格和左一格的最大值，对应情况2，左一格对应就是g,b和g的最大子序列的长度，上一格对应的就是g和g,a的最大子序列的长度

最后就有矩阵:

    g a t c
  0 0 0 0 0
g 0 1 1 1 1
b 0 1 1 1 1
t 0 1 1 2 2
t 0 1 1 2 2

如果是g,a,t,c和g,b,t,c的话，就是

    g a t c
  0 0 0 0 0
g 0 1 1 1 1
b 0 1 1 1 1
t 0 1 1 2 2
c 0 1 1 2 3

2. 最大公共子字符串

根据上面的思路，

2.1. 当ai和bj相等的时候, 若ai-1也不等于bj-1，则当前以ai和bj结尾的最大子字符串就是ai和aj, 为1, 若ai-1和bj-1相等, 则当前以ai和bj结尾的最大子字符串就是ai-1和bj-1长度加1
2.2. 当ai不等于bj的时候, 则当前以ai和bj结尾的最大子字符串长度就是0.

所以对角线加1对应2.1，填0对应2.2

比如
    g a t c
  0 0 0 0 0
g 0 1 0 0 0
b 0 0 0 0 0
t 0 0 0 1 0
c 0 0 0 0 2

以及
    b a b
  0 0 0 0
c 0 0 0 0
a 0 0 1 0
b 0 1 0 2
a 0 0 2 0
'''


def lcs(first, second):
    first_len = len(first)
    second_len = len(second)
    # 矩阵是sec为列, first为行
    matrix = [[0] * (second_len + 1) for _ in range(first_len + 1)]
    max_len = 0
    max_chars = []
    # 这里是每行每一个去比对
    for i in range(first_len):
        for j in range(second_len):
            if first[i] == second[j]:
                current_max = matrix[i][j] + 1
                if current_max > max_len:
                    max_len = current_max
                    max_chars.append(first[i])
            else:
                current_max = max(matrix[i + 1][j], matrix[i][j + 1])
            matrix[i + 1][j + 1] = current_max
    print(max_chars, max_len)
    for i in matrix:
        print(i)
    return


def main():
    data1 = ['G', 'C', 'T', 'A']
    data2 = ['G', 'B', 'T', 'A']
    lcs(data1, data2)
    print('-----------')
    lcs(['G', 'C', 'T', 'A'], ['G', 'B', 'T', 'T'])


if __name__ == '__main__':
    main()
