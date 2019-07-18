#! /usr/bin/python3

# ХешТаблица с закрытой адресацией
class HashMap():
    def __init__(self, N):
        self.size = N
        self.arr = [None] * self.size
        self.nmb = 0

    def hash_(self, x):
        index = hash(x) & (self.size - 1)
        return index

    def add(self, x):
        self.nmb += 1
        index = self.hash_(x)
        print(index, end="	")
        while self.arr[index] is not None:
            index += 1
        self.arr[index] = x
        self.resize()
          
    def remove(self, x):
        index = self.hash_(x)
        while self.arr[index] != x:
            index += 1
        tmp = self.arr[index]
        self.arr[index] = None
        self.nmb -= 1
        return tmp

    def resize(self):
        if self.size <= 10 * self.nmb:
            set_ = set(self.arr)
            set_.remove(None)

            HashMap.__init__(self, self.size * 10)
            print()
            for k in set_:
                self.add(k)
        else:
            return

    def search(self, k):
        index = self.hash_(k)
        while self.arr[index] is not None:
            index += 1
            if self.arr[index] == k:
                return True
        return False


if __name__ == "__main__":
    ht = HashMap(25)
    ht.add(1626363777179)
    ht.add(69969799)
    ht.add(36281847)
    ht.add(8)
    ht.add(0)
    print()
    print(ht.arr, ht.size, sep="\n")
