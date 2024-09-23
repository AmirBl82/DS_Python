# Time Complexity for Node Class is O(1)
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

# Time Complexity of Creating a Circular Linked List with one Node is O(1)
class Circular_linkedList:
    # def __init__(self,value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

# Time Complexity of Creating an empty Circular Linked List is O(1)   
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0    


CLinkedList = Circular_linkedList()
print(CLinkedList)