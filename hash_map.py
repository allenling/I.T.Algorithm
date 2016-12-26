# coding=utf-8

ACTIVE = 0
DUMMY = 1


class Slot(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.status = ACTIVE

    def __repr__(self):
        return '%s:%s:%s' % (self.key, self.value, 'ACTIVE' if not self.status else 'DUMMY')

    def update(self, value):
        self.value = value
        self.status = ACTIVE

    def delete(self):
        self.status = DUMMY


class HashMap(object):

    def __init__(self):
        self.size = 4
        self.csize = 0
        self.data = []
        self.resize()

    def resize(self):
        self.size = self.size * 2
        tmp_data = [_ for _ in self.data]
        self.data = [None] * self.size
        self.csize = 0
        for d in tmp_data:
            if d is None:
                continue
            self.insert(d.key, d.value)

    def insert(self, key, value):
        index = self.search(key)[1]
        if self.data[index] is None:
            self.data[index] = Slot(key, value)
            self.csize += 1
        else:
            self.data[index].update(value)
        if self.size / float(self.csize) <= 1.5:
            self.resize()

    def search(self, key):
        for seq in self.get_hash_seq(key):
            if self.data[seq] is None:
                break
            if self.data[seq].key == key:
                if self.data[seq].status == DUMMY:
                    break
                return True, seq
        return False, seq

    def delete(self, key):
        '''
        记得伪删除
        '''
        is_in, index = self.search(key)
        if is_in:
            self.data[index].status = DUMMY
            return
        raise

    def get_hash_seq(self, key, step=0):
        '''
        两重散列
        '''
        f1 = hash(key) % (self.size - 1)
        if (self.size - 1) % 2 == 0:
            f2 = hash(key) % (self.size - 2)
        else:
            f2 = hash(key) % (self.size - 1)
        while True:
            yield (f1 + step * f2) % (self.size - 1)
            step += 1


def main():
    data = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)]
    hm = HashMap()
    for d in data:
        hm.insert(d[0], d[1])
    print hm.data
    print hm.size
    hm.delete('a')
    print hm.data
    print hm.size
    print hm.search('a')

if __name__ == '__main__':
    main()
