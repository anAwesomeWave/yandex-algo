class MyHeap:
    # Min heap realisation
    def __init__(self):
        self.heap = []

    def push(self, x):
        self.heap.append(x)
        pos = len(self.heap) - 1
        while pos > 0 and self.heap[pos] < self.heap[(pos - 1) // 2]:
            self.heap[pos], self.heap[(pos - 1) // 2] = self.heap[(pos - 1) // 2], self.heap[pos]
            pos = (pos - 1) // 2

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        pos = 0
        while pos * 2 + 2 < len(self.heap):
            min_child = pos * 2 + 1
            if self.heap[min_child] > self.heap[pos * 2 + 2]:
                min_child = pos * 2 + 2
            if self.heap[min_child] < self.heap[pos]:
                self.heap[pos], self.heap[min_child] = self.heap[min_child], self.heap[pos]
                pos = min_child
            else:
                break
        if pos * 2 + 1 < len(self.heap) and self.heap[pos] > self.heap[pos * 2 + 1]:
            self.heap[pos], self.heap[pos * 2 + 1] = self.heap[pos * 2 + 1], self.heap[pos]

    def get(self):
        return self.heap[0]



heap = MyHeap()
heap.push(1)
heap.push(2)
heap.push(3)
heap.push(0)
heap.push(4)
heap.push(-1)
print(heap.heap)