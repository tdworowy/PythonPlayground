class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def height(root,level=[0]):
    if root is None:
        return level[0]-1
    return max(height(root.left,[level[0]+1]),height(root.right,[level[0]+1]))

def height2(root,level):
    if root is None:
        return level -1
    return max(height2(root.left,level+1),height2(root.right,level+1))


def height3(root):
    if root:
        return 1 + max(height(root.left), height(root.right))
    else:
        return -1

if __name__ == "__main__":

    tree = BinarySearchTree()

    arr = [3,2,5,1,4,6,7]
    for i in arr:
        tree.create(i)

    print(height(tree.root))
    print(height2(tree.root,0))
    print(height3(tree.root))