import sys


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def level_order(self, root):
        h = self.height(root)
        for i in range(1, h + 1):
            self.print_given_level(root, i)

    def height(self, node):
        if node is None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def print_given_level(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root.data, end=" ")
        elif level > 1:
            self.print_given_level(root.left, level - 1)
            self.print_given_level(root.right, level - 1)


if __name__ == "__main__":
    myTree = Solution()
    root = None
    for i in [3, 5, 4, 7, 2, 1]:
        data = i
        root = myTree.insert(root, data)
    myTree.level_order(root)
