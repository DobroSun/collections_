#! /usr/bin/python3

class Node():
    def __init__(self, p=None, n=None, v=None):
        self.prev = p
        self.next = n
        self.value = v


class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def addleft(self, x):
        if self.first is None:
            self.first = self.last = Node(None, None, x)
        else:
            p = self.first
            self.first = Node(None, self.first, x)
            p.prev = self.first
        self.size += 1

    def addright(self, x):
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

    def popright(self):
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
        cur = self.first
        while cur is not None:
            if cur.value == k:
                return True
            cur = cur.next
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

    def print_(self):
        if self.first is None:
            print(None)
            return
        print("[")
        cur = self.first
        while cur is not None:
            print(cur.value, end="	")
            cur = cur.next
        print()
        print("]")
        print()
        print("[")

        cur = self.last
        while cur is not None:
            print(cur.value, end="	")
            cur = cur.prev
        print()
        print("]")

    def sort(self):
        for _ in range(self.size):
            cur = self.first
            while cur.next is not None:
                if cur.value > cur.next.value:
                    cur.value, cur.next.value = cur.next.value, cur.value
                cur = cur.next


if __name__ == "__main__":
    queue = Queue()
    queue.addleft(5)
    queue.addleft(2)
    queue.addleft(10)
    queue.addright(9)
    queue.addright(8)
    queue.addleft(4)
    queue.addright(3)
    queue.popright()
    queue.popleft()

    queue.addright(8)
    queue.addleft(4)
    queue.addright(3)
    queue.print_()
    print("-" * 10)
    queue.sort()
    queue.print_()


