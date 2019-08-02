#!/libs/env/bin/python3

class Stack():
    def __init__(self, *args):
        self.arr = []
        self.min = self.max = None
        self.size = 0
    
        self.args = args
        self.create_stack(self.args)

    def __iter__(self):
        return iter(self.arr)

    def __str__(self):
        return str(self.arr)
 
    def __reversed__(self):
        cur = self.size - 1
        while cur >= 0:
            yield self.arr[cur]
            cur -= 1

    def __len__(self):
        return self.size

    def create_stack(self, args):
        if args:
            for iterable in args:
                for num in iterable:
                    self.append(num)
   
    def append(self, x):
        assert type(x) is type(1) or type(x) is type(1.34)
        self.arr.append(x)
        self.size += 1
        if len(self.arr) == 1:
            self.min = self.max = self.arr[0]
        else:
            self.min = x if self.min > x else self.min
            self.max = x if self.max < x else self.max

    def pop(self):
        if self.size != 0:
            tmp = self.arr.pop()
            self.size -= 1
            if self.max == self.min:
                self.max = self.min = None
            elif tmp == self.min:
                self.min = min(self.arr)
            elif tmp == self.max:
                self.max = max(self.arr)
            return tmp
        return


    def sort(self):
        def merge(left, right):
            result = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result += left[i:]
            result += right[j:]
            return result

        def mergesort(list):
            if len(list) < 2:
                return list
            left = mergesort(list[:len(list) // 2])
            right = mergesort(list[len(list) // 2:])
            return merge(left, right)
        self.arr[:] = mergesort(self.arr)
        return self.arr

    def clear(self):
        Stack.__init__(self)

