class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next


    def insert(self,head,data):
        if head is None:
            head = Node(data)
        else:
            current = head
            while current.next:
                current = current.next
            else:
                 current.next = Node(data)
        return head

my_list= Solution()

head=None
for i in [2,3,4,1]:
    data=i
    head = my_list.insert(head, data)
my_list.display(head) # 2 3 4 1

