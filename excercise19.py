class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def count_leaves(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return count_leaves(root.left) + count_leaves(root.right)

root = Node(1)
root.left = Node(6)
root.right = Node(14)

print(count_leaves(root))  
