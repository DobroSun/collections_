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

    def print_(self):
        thislevel = [self.head]
        while thislevel:
            nextlevel = []
            for i in thislevel:
                print(i, end="  ")
                if i.left:
                    nextlevel.append(i)
                if i.right:
                    nextlevel.append(i)
                thislevel = nextlevel







    def print_levels(self):
        # Работает только при отсутствии повторяемых ключей.
        self.dis = dict(sorted(self.dis.items(), key=lambda x: x[1]))
        tmp_dis = 0
        for i in self.dis:
            if tmp_dis == self.dis[i]:
                print(i, end="  ")
            else:
                print()
                print(i, end="   ")
            tmp_dis = self.dis[i]
    
    
    
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
    tree.print_()
