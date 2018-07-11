def combination_sum(nlist, target):
    '''
    思路是回溯, 但是没看懂
    '''
    if not nlist:
        return []
    res = []
    sum_list = [[[], 0]]
    new_nlist = sorted(nlist)
    for number in new_nlist:
        len_sum_list = len(sum_list)
        for i in range(len_sum_list):
            key, value = sum_list[i]
            while True:
                value += number
                key = key + [number]
                if value < target:
                    sum_list.append([key, value])
                elif value == target:
                    res.append(key)
                    break
                else:
                    break
    return res


def main():
    datas = [[[2, 3, 5], 8],
             [[2, 3, 6, 7], 7],
             ]
    for data, target in datas:
        print(combination_sum(data, target))
    return


if __name__ == '__main__':
    main()
