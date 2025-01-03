class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, dataType = int):
        self.head = None
        self.dataType = dataType
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " <-> "
            temp_node = temp_node.next
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
            self.head = new_node
            self.length += 1
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node
        self.length += 1

    def delete(self, deleted_node):
        if deleted_node is None:
            raise ValueError("Cannot delete a Null Node")
        
        if self.head == deleted_node:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            self.length -= 1
            return
        
        current_node = self.head
        while current_node.next:
            if current_node.next == deleted_node:
                current_node.next.next.prev = current_node
                current_node.next = deleted_node.next
                self.length -= 1
                return
            current_node = current_node.next



dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
print(dll)
node = dll.head.next.next.next.prev
dll.delete(node)
print(dll)