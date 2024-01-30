# '''
#
#  [val, [left], [right]]
# '''

class Tree:
    def __init__(self):
        self.tree = None

    def add(self, value):
        if not self.tree:
            self.tree = [value, None, None]
            return

        def rec_add(node):
            if node[0] == value:
                return
            elif node[0] > value:
                if not node[1]:
                    node[1] = [value, None, None]
                else:
                    rec_add(node[1])
            else:
                if not node[2]:
                    node[2] = [value, None, None]
                else:
                    rec_add(node[2])

        rec_add(self.tree)

    def left_traversal(self):
        def rec_left_traversal(node):
            if node[1] is not None:
                flag = 0
                rec_left_traversal(node[1])
            if node[1] and node[2]:
                print(node[0])
            if node[2] is not None:
                flag = 0
                rec_left_traversal(node[2])
        rec_left_traversal(self.tree)


tree1 = Tree()

arr = list(map(int, input().split()))

for x in arr[:-1]:
    tree1.add(x)
tree1.left_traversal()
