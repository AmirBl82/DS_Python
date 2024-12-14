class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self, dataType=int):
        self.__head = None
        self.__tail = None
        self.__length = 0
        self.dataType = dataType
    
    def __str__(self):
        if not self.__head:
            return "Circular Linked List is Empty"
        result = ""
        temp_node = self.__head
        while True:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.__head:
                break
            result += " -> "
        return result
    
    def get_length(self):
        return self.__length
    
    def insert(self, index, value):
        if not isinstance(value, self.dataType):
            raise TypeError(f"Linked List only accepts elements of type {self.dataType}")
        
        if index < 0 or index > self.__length:
            raise IndexError("Index out of Bounds")
        
        new_node = Node(value)
        if index == 0:
            if not self.__head:  # Inserting into an empty list
                self.__head = self.__tail = new_node
                new_node.next = self.__head
            else:
                new_node.next = self.__head
                self.__head = new_node
                self.__tail.next = self.__head
        else:
            temp_node = self.__head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            if index == self.__length:  # Update tail if appended
                self.__tail = new_node
        
        self.__length += 1
    
    def append(self, value):
        self.insert(self.__length, value)
    
    def prepend(self, value):
        self.insert(0, value)
    
    def get_first(self):
        if self.__head:
            return self.__head
        return "Circular Linked List is Empty"
    
    def get_index(self, value):
        current_node = self.__head
        index = 0
        while True:
            if current_node.value == value:
                return index
            current_node = current_node.next
            index += 1
            if current_node == self.__head:
                break
        raise ValueError("Element does not exist")
    
    def get_value(self, index):
        if index < 0 or index >= self.__length:
            raise IndexError("Index out of bounds")
        current_node = self.__head
        for _ in range(index):
            current_node = current_node.next
        return current_node.value
    
    def get_address(self, value):
        current_node = self.__head
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
    
    def delete_byIndex(self, index):
        if index < 0 or index >= self.__length:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            deleted_node = self.__head
            if self.__length == 1:  # Only one element
                self.__head = self.__tail = None
            else:
                self.__head = self.__head.next
                self.__tail.next = self.__head
        else:
            prev_node = self.__head
            for _ in range(index - 1):
                prev_node = prev_node.next
            deleted_node = prev_node.next
            prev_node.next = deleted_node.next
            if index == self.__length - 1:  # Update tail if last node is deleted
                self.__tail = prev_node
        
        deleted_node.next = None
        self.__length -= 1
        return deleted_node
    
    def delete_byValue(self, x):
        if x is None:
            raise ValueError("x Cannot be None")
        if self.__head is None:
            raise ValueError("Circular Linked List is empty")

        try:
            index = self.get_index(x)
            self.delete_byIndex(index)
        except ValueError:
            raise ValueError("Value not found in the Circular Linked List")
    
    def delete_byAddress(self, deleted_node):
        if deleted_node is None:
            raise ValueError("Node cannot be None")
        if self.__head is None:
            raise ValueError("Circular Linked List is empty")
        
        if deleted_node == self.__head:
            return self.delete_byIndex(0)
        
        prev_node = self.__head
        while prev_node.next != deleted_node:
            prev_node = prev_node.next
            if prev_node == self.__head:  # Node not found
                raise ValueError("Node not found in the Circular Linked List")
        
        prev_node.next = deleted_node.next
        if deleted_node == self.__tail:
            self.__tail = prev_node
        
        deleted_node.next = None
        self.__length -= 1
        return deleted_node
    
    def delete_byPrevAddress(self, prev_node):
        if prev_node is None or prev_node.next is None:
            raise ValueError("Invalid previous node or empty next reference")
        if self.__head is None:
            raise ValueError("Circular Linked List is empty")
        
        deleted_node = prev_node.next
        prev_node.next = deleted_node.next
        if deleted_node == self.__head:
            self.__head = deleted_node.next
        if deleted_node == self.__tail:
            self.__tail = prev_node
        
        deleted_node.next = None
        self.__length -= 1
        return deleted_node

