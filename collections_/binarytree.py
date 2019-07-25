#! usr/bin/python3

class Node():
    def __init__(self, k, v):
        self.key = k
        self.value = v

        self.left = None
        self.right = None
        self.parent = None


# Двоичное дерево без балансировок.
class BinaryTree():
    def __init__(self):
        self.head = None
        self.size = 0
        self.dis = {}

    def add(self, k, v):
        self.size += 1
        if self.head is None:
            self.head = Node(k, v)
            self.dis = {k: 0}
        else:
            cur = self.head
            while cur is not None:
                prev = cur
                cur = cur.right if k >= cur.key else cur.left
            cur = Node(k, v)
            self.dis[cur.key] = self.dis[prev.key] + 1
            cur.parent = prev
            prev.right = cur if cur.key >= prev.key else prev.right
            prev.left = cur if cur.key < prev.key else prev.left

    def print_keys(self):
        from queue import Queue
        q = Queue()
        q.addright(self.head)
        count = 1
        print(self.head.key)
        while q.size:
            iteration = 0
            for _ in range(count):
                if iteration == 0:
                    count = 0 
                cur = q.popleft()
                if cur is None:
                    return
                if [cur.left, cur.right] == [None, None]:
                    continue
                for nei in [cur.left, cur.right]:
                    if nei is not None:
                        q.addright(nei)
                        count += 1 
                iteration += 1
            tmp = q.first
            while tmp is not None:
                print(tmp.value.key, end="  ")
                tmp = tmp.next
            print()

    def pop(self, k):
        cur = self.head
        while cur is not None:
            if cur.key == k:
                tmp = cur.value
                break
            prev = cur
            cur = cur.right if k >= cur.key else cur.left
        if cur.left:
            next_ = cur.left
            prev_ = None
            while next_.right:     # Поиск самого большего в левой ветви
                prev_ = next_ 
                next_ = next_.right
            next_ = cur

            next_.left = cur.left
            next_.right = cur.right
            next_.parent = None if cur.key == self.head.key else prev

            cur = None
            if prev_:
                prev_.right = None
        elif cur.right:
            next_ = cur.right
            prev_ = None
            while next_.left:     # Поиск самого меньшего в правой ветви
                prev_ = next_ 
                next_ = next_.left
            next_ = cur

            next_.left = cur.left
            next_.right = cur.right
            next_.parent = None if cur.key == self.head.key else prev

            cur = None
            if prev_:
                prev_.left = None 
        else:
            cur = None
            prev.right = None if prev.right.key == k else prev.right
            prev.left = None if prev.left.key == k else prev.left
                
        self.size -= 1 
        return tmp




    def search(self, k):
        cur = self.head
        while cur is not None:
            if cur.key == k:
                return True
            cur = cur.right if k >= cur.key else cur.left
        return False


if __name__ == "__main__":
    tree = BinaryTree()
    tree.add(3, "3")
    tree.add(7, "7")
    tree.add(8, "8")
    tree.add(4, "4")
    tree.add(0, "0")
    tree.add(1, "1")
    tree.add(9, "9")
    tree.add(2, "2")
    tree.print_keys()
    tree.pop(3)
    tree.print_keys()
