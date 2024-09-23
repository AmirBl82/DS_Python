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
    
    # Showing Circular Linked List in str
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' -> '
        return result
    
    # Insert an Element at the end of Circular Linked List
    # Time Complexity is O(1)
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1




CLinkedList = Circular_linkedList()
CLinkedList.append(10)
CLinkedList.append(20)
print(CLinkedList.head.value)
print(CLinkedList.tail.value)
print(CLinkedList)