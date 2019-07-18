#! usr/bin/python3

class Heap():
  def __init__(self):
    self.arr = []
  
  def add(self, x):
    self.arr.append(x)
    i = len(self.arr) - 1
    while self.arr[(i-1) // 2] < self.arr[i] and i != 0:
      self.arr[i], self.arr[(i-1) // 2] = self.arr[(i-1) // 2], self.arr[i]
      i = (i-1) // 2


  def pop(self):
    tmp = self.arr[0]
    self.arr[0] = self.arr[-1]
    
    self.arr.pop()
    i = 0
    while len(self.arr) >= i*2 + 1 and \
              (self.arr[i*2 + 1] > self.arr[i] or (self.arr[i*2 + 2] > self.arr[i])):
      if self.arr[i*2 + 1] >= self.arr[i*2 + 2]:
        self.arr[i], self.arr[i*2 + 1] = self.arr[i*2 + 1], self.arr[i]
        i = i*2 + 1
      else:
        self.arr[i], self.arr[i*2 + 2] = self.arr[i*2 + 2], self.arr[i]
        i = i*2 + 2
    return tmp


if __name__ == "__main__":
  heap = Heap()
  heap.add(3)
  heap.add(5)
  heap.add(2)
  heap.add(6) 
  heap.add(8) 
  heap.add(2)  
  heap.add(0)
  print(heap.arr)
  print(heap.pop())
  print(heap.arr)
  
  
