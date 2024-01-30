class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.next = right
        self.prev = left



n1 = Node(1, Node())

n2 = n1

print(id(n2), id(n1))
n2 = 123

print(n1)