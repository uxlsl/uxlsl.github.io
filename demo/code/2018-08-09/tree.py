class Node(object):
    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val

    def IsSame(self, node):
        if node is None or self.val != node.val:
            return False
        if (self.left is None and node.left is not None) \
                or (self.left is not None and node.left is None):
            return False
        if (self.right is None and node.right is not None) \
                or (self.right is not None and node.right is None):
            return False
        return (self.left.IsSame(node.left)
                if self.left is not None else True) \
            and (self.right.IsSame(node.right)
                 if self.right is not None else True)
