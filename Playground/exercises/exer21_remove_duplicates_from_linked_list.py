class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while start.next != None:
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next

    def remove_duplicates(self, head):
        data = set()
        current = head
        new_head = None
        while current:
            if current.data not in data:
                data.add(current.data)
                new_head = self.insert(new_head, current.data)
            current = current.next
        return new_head


if __name__ == "__main__":
    my_list = Solution()
    head = None
    for i in [1, 2, 2, 3, 3, 4]:
        data = i
        head = my_list.insert(head, data)
    head = my_list.remove_duplicates(head)
    my_list.display(head)
