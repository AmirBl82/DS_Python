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
        while current_node.next:
            if current_node.next.value == value:
                return current_node.next
            current_node = current_node.next
        raise ValueError("Element does not exist")
    
    def set_value(self, index, value):
        if not isinstance(value, self.dataType):
            raise TypeError(f"Linked List only accepts elements of type {self.dataType}")
        current_node = self.get_value(index)
        if current_node:
            current_node.value = value
            return True
        return False
    
    def append(self, value):
        if not isinstance(value, self.dataType):
            raise TypeError(f"Linked List only accepts elements of type {self.dataType}")
        
        new_node = Node(value)
        if self.head == None:
            self.head = self.tail = new_node
            new_node.next = new_node.prev = self.head
            self.length += 1
            return
        
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next
        current_node.next = new_node
        new_node.next = self.head
        self.head.prev = new_node
        self.tail = new_node
        self.length += 1
    
    def delete(self, deleted_node):
        if deleted_node is None:
            raise ValueError("Cannot delete a Null Node")
        
        if deleted_node == self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = self.tail
                self.tail.next = self.head
            self.length -= 1
            return
        
        current_node = self.head
        while current_node.next != self.head:
            if current_node.next == deleted_node:
                current_node.next.next.prev = current_node
                current_node.next = deleted_node.next
                if deleted_node == self.tail:
                    self.tail = current_node
                self.length -= 1
                return
            current_node = current_node.next


cdll = CircularDoublyLinkedList()
cdll.append(1)
cdll.append(2)
cdll.append(3)
cdll.append(4)
print(cdll)
node = cdll.tail
cdll.delete(node)
print(cdll)
print(cdll.tail.next.value)
print(cdll.get_address(2).value)