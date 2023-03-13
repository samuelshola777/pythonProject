class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end="->")
            temp = temp.next


    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self,value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node

    # def apend(self,value):
    #     new_node = Node(value)
    #     # temp = self.head
    #     #
    #     # while temp.next is not None:
    #     #     temp = temp.next
    #     #
    #     # temp.next = new_node
    #     new_node.next = self.tail
    #     self.tail = new_node

list = LinkedList()
list.prepend(9)
list.prepend(5)
list.prepend(6)
print(list.head.value)



new_node = Node(6)
print(list.tail(7))
print(list.head(4))