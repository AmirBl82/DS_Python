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
        if self.__head is None:
            return "Circular Linked List is empty"
        
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
            raise TypeError(f"Circular Linked List only accepts elements of type {self.dataType}")
        if index < 0 or index > self.__length:
            raise IndexError("Index out of bounds")

        new_node = Node(value)
        if index == 0:  # Insert at the head
            if self.__head is None:  # List is empty
                self.__head = new_node
                self.__tail = new_node
                new_node.next = new_node  # Point to itself
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
            if temp_node == self.__tail:  # If inserted at the end, update tail
                self.__tail = new_node

        self.__length += 1

    def append(self, value):
        self.insert(self.__length, value)

    def prepend(self, value):
        self.insert(0, value)

    def get_first(self):
        if self.__head:
            return self.__head
        return "Circular Linked List is empty"

    def get_index(self, value):
        if self.__head is None:
            raise ValueError("Circular Linked List is empty")
        
        current_node = self.__head
        index = 0
        while True:
            if current_node.value == value:
                return index
            current_node = current_node.next
            index += 1
            if current_node == self.__head:  # Looped back to start
                break
        raise ValueError("Element does not exist")

    def get_value(self, index):
        if index < 0 or index >= self.__length:
            raise IndexError("Index out of bounds")
        current_node = self.__head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def set_value(self, index, value):
        if not isinstance(value, self.dataType):
            raise TypeError(f"Circular Linked List only accepts elements of type {self.dataType}")
        temp_node = self.get_value(index)
        if temp_node:
            temp_node.value = value
            return True
        return False

    def delete_byIndex(self, index):
        if index < 0 or index >= self.__length:
            raise IndexError("Index out of bounds")
        if index == 0:  # Delete the head
            deleted_node = self.__head
            if self.__length == 1:  # Only one node in the list
                self.__head = None
                self.__tail = None
            else:
                self.__head = self.__head.next
                self.__tail.next = self.__head
        else:
            temp_node = self.__head
            for _ in range(index - 1):
                temp_node = temp_node.next
            deleted_node = temp_node.next
            temp_node.next = deleted_node.next
            if deleted_node == self.__tail:  # If deleting the tail
                self.__tail = temp_node

        deleted_node.next = None
        self.__length -= 1
        return deleted_node

    def delete_byValue(self, value):
        index = self.get_index(value)
        return self.delete_byIndex(index)

def copy_CLL(org_CLL):
    new_CLL = CircularLinkedList(org_CLL.dataType)
    if org_CLL.get_length() == 0:
        return new_CLL
    
    current_node = org_CLL.get_first()
    for _ in range(org_CLL.get_length()):
        new_CLL.append(current_node.value)
        current_node = current_node.next
    return new_CLL
