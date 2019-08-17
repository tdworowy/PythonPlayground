class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root is None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root


    def __get_height(self, root):
        if root is None:
            return 0
        else:
            return max(self.__get_height(root.left), self.__get_height(root.right)) + 1

    def get_height(self, root):
        return self.__get_height(root) - 1

T= [7,3,5,2,1,4,6,7]
my_tree=Solution()
root=None
for i in T:
    data=i
    root = my_tree.insert(root, data)
height = my_tree.get_height(root) - 1
print(height)