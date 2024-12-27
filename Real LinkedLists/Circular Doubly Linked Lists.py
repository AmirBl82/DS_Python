class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
class CircularDoublyLinkedList:
    def __init__(self, dataType = int):
        self.head = None
        self.tail = None
        self.dataType = dataType
        self.length = 0

    def __str__(self):
        if not self.head:
            return "List is empty"
        result = []
        temp_node = self.head
        while True:
            result.append(str(temp_node.value))
            temp_node = temp_node.next
            if temp_node == self.head:  
                break
        return " <-> ".join(result)    
    

    def get_value(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node    

    def get_address(self, value):
        current_node = self.head
        for _ in range(self.length):
            if current_node.value == value:
                return current_node
            current_node = current_node.next
        raise ValueError("Element does not exist")

    def set_value(self, index, value):
        if not isinstance(value, self.dataType):
            raise TypeError(f"Circular Doubly Linked List only accepts elements of type {self.dataType}")
        node = self.get_value(index)
        node.value = value
    
    def append(self, value):
        if not isinstance(value, self.dataType):
            raise TypeError(f"Circular Doubly Linked List only accepts elements of type {self.dataType}")
        
        new_node = Node(value)
        if self.head == None:
            self.head = self.tail = new_node
            new_node.next = new_node.prev = self.head
        
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node
        self.length += 1
    
    def delete(self, deleted_node):
        if deleted_node is None:
            raise ValueError("Cannot delete a null Node")
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            if self.head == deleted_node:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
            elif self.tail == deleted_node:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
            else:
                deleted_node.next.prev = deleted_node.next
                deleted_node.prev.next = deleted_node.next
        self.length -= 1

cdll = CircularDoublyLinkedList()
cdll.append(1)
cdll.append(2)
cdll.append(3)
cdll.append(4)
print(cdll)
node = cdll.tail.next.next
cdll.delete(node)
print(cdll)