from binarytree import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def lca(root, v1, v2):
    node = root
    while node:
        if max(v1, v2) < node.value:
            node = node.left
        elif min(v1, v2) > node.value:
            node = node.right
        else:
            break
    return node


if __name__ == "__main__":
    tree = BinarySearchTree()
    arr = [9, 7, 8, 5, 6, 4, 3, 1]

    for i in arr:
        tree.create(i)

    v = [1, 6]

    ans = lca(tree.root, v[0], v[1])
    print(ans.value)
    print(tree.root)
