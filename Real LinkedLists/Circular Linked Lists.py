class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class CircularLinkedList:
    def __init__(self, dataType = int):
        self.head = None
        self.tail = None
        self.length = 0
        self.dataType = dataType
    
    def __str__(self):
        if not self.head:
            return "Circular Linked List is Empty"
        result = ""
        temp_node = self.head
        while True:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += " -> "
        return result

    
    def get_value(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node
    
    def get_address(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.next
        raise ValueError("Element does not exist")
    
    def set_value(self, index, value):
        if not isinstance(value, self.dataType):
            raise TypeError(f"Linked List only accepts elements of type {self.dataType}")
        temp_node = self.get_value(index)
        if temp_node:
            temp_node.value = value
            return True
        return False
    
    def append(self, value):
        if not isinstance(value, self.dataType):
            raise TypeError(f"Circular Linked List only accepts elements of type {self.dataType}")
        
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    def delete(self, deleted_node):
        if deleted_node is None:
            raise ValueError("Cannot delete a Null Node")
        
        if deleted_node == self.head:
            self.head = self.head.next
            self.tail.next = self.head
            self.length -= 1
            return

        current_node = self.head
        while current_node.next != self.head:  
            if current_node.next == deleted_node:
                current_node.next = current_node.next.next
                if current_node.next == self.head:  
                    self.tail = current_node
                self.length -= 1
                return
            current_node = current_node.next


cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)
print(cll.length)
node = cll.head.next.next.next
cll.delete(node)
print(cll)
print(node)
print(cll.length)