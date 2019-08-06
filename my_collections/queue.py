#!/usr/bin/env python3

class Node():
    def __init__(self, p=None, n=None, v=None):
        self.prev = p
        self.next = n
        self.value = v


class Queue():
    def __init__(self, *args):
        self.first = None
        self.last = None
        self.size = 0
        
        self.args = args
        self._create_queue(self.args)

    def __iter__(self):
        cur = self.first
        while cur is not None:
            yield cur.value
            cur = cur.next
    
    def __reversed__(self):
        cur = self.last
        while cur is not None:
            yield cur.value
            cur = cur.prev

    def __len__(self):
        return self.size

    def __str__(self):
        L = []
        for i in self:
            L.append(i)
        return str(L)

    def _create_queue(self, args):
        if args:
            for iterable in args:
                for num in iterable:
                    self.append(num)
    
    def addleft(self, x):
        if self.first is None:
            self.first = self.last = Node(None, None, x)
        else:
            p = self.first
            self.first = Node(None, self.first, x)
            p.prev = self.first
        self.size += 1

    def append(self, x):
        if self.first is None:
            self.first = self.last = Node(None, None, x)
        else:
            p = self.last
            self.last = Node(self.last, None, x)
            p.next = self.last
        self.size += 1

    def popleft(self):
        if self.size == 1:
            self.size -= 1
            tmp = self.first.value
            self.first = None
            return tmp
        if self.first is not None:
            p = self.first.value
            next_node = self.first.next
            next_node.prev = None
            self.first = next_node
            self.size -= 1
            return p

    def pop(self):
         if self.size == 1:
            self.size -= 1
            tmp = self.first.value
            self.first = None
            return tmp
         if self.first is not None:
            p = self.last.value
            prev_node = self.last.prev
            prev_node.next = None
            self.last = prev_node
            self.size -= 1
            return p
    
    def pop_k(self, k):
        cur = self.first
        while cur is not None:
            if cur.value == k and cur == self.first == self.last:
                self.first = self.last = None
                self.siz -= 1
                return k
            elif cur.value == k and cur == self.first:
                cur.next.prev = None
                self.first = cur.next
                self.size -= 1
                return k
            elif cur.value == k and cur == self.last:
                cur.prev.next = None
                self.last = cur.prev
                self.size -= 1
                return k
            elif cur.value == k:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                cur = None
                self.size -= 1
                return k
            else:
                cur = cur.next


    def search(self, k):
        for i in self:
            if i == k:
                return True
        return False

    def reverse(self):
        cur = self.first
        while cur is not None:
            tmp = cur.next
            if cur.prev is None:
                cur.next = None
                self.last = cur
            else:
                cur.next = cur.prev
                cur.prev.prev = cur
                cur.prev = None
                self.first = cur
            cur = tmp

    def sort(self):
        for _ in range(self.size):
            cur = self.first
            while cur.next is not None:
                if cur.value > cur.next.value:
                    cur.value, cur.next.value = cur.next.value, cur.value
                cur = cur.next

    def clear(self):
        Queue.__init__(self)

