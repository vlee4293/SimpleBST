import random


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.root = None

    def _get_height_helper(self, subtree):
        if subtree is None:
            return 0
        else:
            return 1+max(self._get_height_helper(subtree.left), self._get_height_helper(subtree.right))

    def _balanced_add(self, subtree, node):
        if subtree is None:
            return node
        else:
            if self._get_height_helper(subtree.left) > self._get_height_helper(subtree.right):
                subtree.right = self._balanced_add(subtree.right, node)
            else:
                subtree.left = self._balanced_add(subtree.left, node)
            return subtree

    def _move_up(self, subtree):
        if self._get_height_helper(subtree.left) > self._get_height_helper(subtree.right):
            subtree.data = subtree.left.data
            subtree.left = self._move_up(subtree.left)
            return subtree
        else:
            if subtree.right is not None:
                subtree.data = subtree.right.data
                subtree.right = self._move_up(subtree.right)
                return subtree
            else:
                return None

    def _remove_value(self, subtree, target):
        if subtree is None:
            return subtree
        if subtree.data == target:
            return self._move_up(subtree)
        else:
            subtree.left = self._remove_value(subtree.left, target)
            subtree.right = self._remove_value(subtree.right, target)
            return subtree

    def get_height(self):
        return self._get_height_helper(self.root)

    def insert(self, data):
        node = Node(data)
        self.root = self._balanced_add(self.root, node)

    def remove(self, target):
        self.root = self._remove_value(self.root, target)

    def _preorder(self, visit, subtree, **kwargs):
        if subtree is not None:
            visit(subtree.data, **kwargs)
            self._preorder(visit, subtree.left, **kwargs)
            self._preorder(visit, subtree.right, **kwargs)

    def _inorder(self, visit, subtree, **kwargs):
        if subtree is not None:
            self._inorder(visit, subtree.left, **kwargs)
            visit(subtree.data, **kwargs)
            self._inorder(visit, subtree.right, **kwargs)

    def _postorder(self, visit, subtree, **kwargs):
        if subtree is not None:
            self._postorder(visit, subtree.left, **kwargs)
            self._postorder(visit, subtree.right, **kwargs)
            visit(subtree.data, **kwargs)

    def preorder(self, visit, **kwargs):
        self._preorder(visit, self.root, **kwargs)

    def inorder(self, visit, **kwargs):
        self._inorder(visit, self.root, **kwargs)

    def postorder(self, visit, **kwargs):
        self._postorder(visit, self.root, **kwargs)


class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def _place(self, subtree, node):
        if subtree is None:
            return node
        elif subtree.data > node.data:
            subtree.left = self._place(subtree.left, node)
        else:
            subtree.right = self._place(subtree.right, node)
        return subtree

    def _remove_value(self, subtree, target):
        if subtree is None:
            return subtree
        elif subtree.data == target:
            return self._remove_node(subtree)
        elif subtree.data > target:
            subtree.left = self._remove_value(subtree.left, target)
        else:
            subtree.right = self._remove_value(subtree.right, target)
        return subtree

    def _remove_node(self, node):
        if node.left is None and node.right is None:
            return None
        elif (node.left is not None) != (node.right is not None):
            if node.left is not None:
                return node.left
            else:
                return node.right
        else:
            node.right, node.data = self._remove_leftmost(node.right)
            return node

    def _remove_leftmost(self, subtree):
        if subtree.left is None:
            return self._remove_node(subtree), subtree.data
        else:
            subtree.left, _ = self._remove_leftmost(subtree.left)
            return subtree

    def insert(self, data):
        self.root = self._place(self.root, Node(data))

    def remove(self, target):
        self.root = self._remove_value(self.root, target)


tree = BinarySearchTree()
random.seed(1)
sample = [round(random.normalvariate(50, 25), 0) for _ in range(5)]
print(sample)
for i in sample:
    tree.insert(i)
tree.preorder(print, end=" ")

