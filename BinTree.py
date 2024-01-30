class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        def rec_add(node, depth):
            if node.val == value:
                return
            if value < node.val:
                if node.left is None:
                    node.left = Node(value)
                    return depth + 1
                else:
                    return rec_add(node.left, depth + 1)
            else:
                if node.right is None:
                    node.right = Node(value)
                    return depth + 1
                else:
                    return rec_add(node.right, depth + 1)

        if self.root is None:
            self.root = Node(value)
            return 1
        return rec_add(self.root, 1)

    def search(self, value):
        def rec_search(node):
            if node is None:
                return False
            if node.val == value:
                return True
            elif node.val > value:
                return rec_search(node.right)
            else:
                return rec_search(node.left)

        return rec_search(self.root)

    def find_max_depth(self):
        def rec_find_max_depth(node, depth=0):
            if node is None:
                return depth
            return max(
                rec_find_max_depth(node.left, depth + 1),
                rec_find_max_depth(node.right, depth + 1)
            )

        return rec_find_max_depth(self.root)


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


arr = list(map(int, input().split()))
tree = BinaryTree()
for x in arr:
    if x == 0:
        break
    res = tree.add(x)
    if res is not None:
        print(res, end=' ')
