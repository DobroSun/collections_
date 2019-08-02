#!/libs/env/bin/python3

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
        else:
            cur = self.head
            while cur is not None:
                prev = cur
                cur = cur.right if k >= cur.key else cur.left
            cur = Node(k, v)
            cur.parent = prev
            prev.right = cur if cur.key >= prev.key else prev.right
            prev.left = cur if cur.key < prev.key else prev.left
            
            self.check_balance(cur)

    def print_keys(self):
        if not self.size:
            print('')
            return
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
        if not self.size:
            return
        cur = self.head
        prev = self.head.parent
        while cur is not None:
            if cur.key == k:
                tmp = cur.value
                break
            prev = cur
            cur = cur.right if k >= cur.key else cur.left
        if self.head.key == k:
            if cur.left:
                next_ = cur.left
                prev_ = None
                while next_.right:     # Поиск самого большего в левой ветви
                    prev_ = next_ 
                    next_ = next_.right
             
                next_.left = cur.left
                next_.right = cur.right
                next_.parent = None if cur.key == self.head.key else prev
                
                self.head = next_
                
                cur.right = None
                cur.parent = None
                cur.left = None
                del cur

                if prev_:
                    prev_.right = None

 
            elif cur.right:
                next_ = cur 
                prev_ = None
                while next_.left:     # Поиск самого меньшего в правой ветви
                    prev_ = next_ 
                    next_ = next_.left
            
                next_.left = cur.left
                next_.right = cur.right
                next_.parent = None if cur.key == self.head.key else prev
               
                self.head = next_
               
                cur.right = None
                cur.parent = None
                cur.left = None
                del cur

                if prev_:
                    prev_.left = None
            else:
                self.head = None

                cur.right = None
                cur.parent = None
                cur.left = None
                del cur
        else:
            if cur.left:
                next_ = cur.left
                next_.right = cur.right
                next_.parent = cur.parent
                 
                cur.right = None
                cur.parent = None
                cur.left = None
                del cur 

                if prev.left:
                    prev.left = next_ if prev.left.key == k else prev.left
                if prev.right:
                    prev.right = next_ if prev.right.key == k else prev.right

            elif cur.right:
                next_ = cur.right
                next_.left = cur.left
                next_.parent = cur.parent
                 
                cur.right = None
                cur.parent = None
                cur.left = None
                del cur 
               
                if prev.left:
                    prev.left = next_ if prev.left.key == k else prev.left
                if prev.right:
                    prev.right = next_ if prev.right.key == k else prev.right                
            else:
                cur.right = None
                cur.parent = None
                cur.left = None
                del cur 
                
                if prev.left:
                    prev.left = None if prev.left.key == k else prev.left
                if prev.right:
                    prev.right = None if prev.right.key == k else prev.right                 
                
        self.size -= 1 
        return tmp

    def print_in_line(self):
        if not self.size:
            print('')
            return
        from stack import Stack
        from queue import Queue
        q = Queue()
        q.addright(self.head)
        A = Stack()
        A.append(self.head.key)
        while q.size:
            cur = q.popleft()
            for nei in [cur.left, cur.right]:
                if nei is not None:
                    q.addright(nei)
                    A.append(nei.key)
        return A.arr
    
    def height(self, node_key=None):
        node_key = node_key or self.head.key
        if self.search(node_key):
            cur = self.head
            while cur is not None:
                if cur.key == node_key:
                    break
                cur = cur.right if node_key >= cur.key else cur.left
        else: 
            cur = Node(node_key, node_key)
            cur.right = None
            cur.left = None
        def dfs(vertex, dis, dict_):
            dict_[vertex.key] = dis
            for new_vert in [vertex.left, vertex.right]:
                if new_vert is not None:
                    new_dis = dict_[vertex.key] + 1
                    dfs(new_vert, new_dis, dict_)
            dict_ = dict(sorted(dict_.items(), key=lambda x: x[1], reverse=True))
            for key in dict_:
                return dict_[key]
        left_h = dfs(cur.left, 1, {}) if cur.left else 0
        right_h = dfs(cur.right, 1, {}) if cur.right else 0
        return left_h, right_h

    def check_balance(self, node):
        def check_height(node):
            left_h, right_h = self.height(node.key)
            side = 'left' if left_h > right_h else 'right'
            if max(left_h, right_h) - min(left_h, right_h) > 1:
                self.balance(node, side)
        
        while node.parent is not None:
            node = node.parent
            check_height(node)
    
    def balance(self, node, side):
        prev = node.parent
        branch = side if prev == None else ""
        if prev:
            branch = 'left' if node.key < self.head.key else 'right'        

        # крайнее правое
        if side == branch and side == 'right': 
            self.small_left_turn(node)
       
        # крайнее левое 
        elif side == branch and side == 'letf':            
            self.small_right_turn(node)
        
        # правое центральное
        elif side != branch and side == 'right': 
            self.big_left_turn(node)
        
        # левое центральное 
        elif side != branch and side == 'left': 
            self.big_right_turn(node)
   
    def small_left_turn(self, node):
        print("Small_left_turn balancing")
        cur = node
        prev = cur.parent
        
        next_ = cur.right
        if prev:
            prev.right = next_
        
        cur.right = next_.left
        next_.left = cur
        cur.parent = next_
        next_.parent = prev
        
        if cur == self.head:
            self.head = next_
            
        if cur.right:            
            cur.right.parent = cur

    def small_right_turn(self, node):
        print("Small_right_turn balancing")
        cur = node
        prev = cur.parent
        
        next_ = cur.left
        if prev:
            prev.left = next_
        
        cur.left = next_.right
        next_.right = cur
        cur.parent = next_
        next_.parent = prev
        
        if cur == self.head:
            self.head = next_
            
        if cur.left:            
            cur.left.parent = cur


    def search(self, k):
        if k == None:
            return False

        cur = self.head
        while cur is not None:
            if cur.key == k:
                return True
            cur = cur.right if k >= cur.key else cur.left
        return False
    
    
    
if __name__ == "__main__":
    tree = BinaryTree()
    print('-' * 100)
    print(tree.search(None)) 
    print('-' * 100)
    tree.add(3, "3")
    tree.add(7, "7")
    tree.add(8, "8")

    tree.add(2, "2")
    print(tree.print_in_line())
    tree.add(1, "1")
    tree.add(7, "7")
    tree.add(8, "8")

    tree.print_keys()
    print(tree.print_in_line())
