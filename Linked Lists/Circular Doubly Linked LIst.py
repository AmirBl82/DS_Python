class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self, dataType=int):
        self.__head = None
        self.__tail = None
        self.__length = 0
        self.dataType = dataType

    def __str__(self):
        if self.__head is None:
            return "Circular Doubly Linked List is empty"
        
        result = ""
        temp_node = self.__head
        while True:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.__head:
                break
            result += " <-> "
        return result

    def get_length(self):
        return self.__length

    def insert(self, index, value):
        if not isinstance(value, self.dataType):
            raise TypeError(f"Circular Doubly Linked List only accepts elements of type {self.dataType}")
        if index < 0 or index > self.__length:
            raise IndexError("Index out of bounds")

        new_node = Node(value)
        if self.__length == 0:  # Insert in empty list
            self.__head = new_node
            self.__tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        elif index == 0:  # Insert at the head
            new_node.next = self.__head
            new_node.prev = self.__tail
            self.__head.prev = new_node
            self.__tail.next = new_node
            self.__head = new_node
        elif index == self.__length:  # Insert at the tail
            new_node.prev = self.__tail
            new_node.next = self.__head
            self.__tail.next = new_node
            self.__head.prev = new_node
            self.__tail = new_node
        else:  # Insert in the middle
            temp_node = self.__head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            new_node.prev = temp_node
            temp_node.next.prev = new_node
            temp_node.next = new_node
        
        self.__length += 1

    def append(self, value):
        self.insert(self.__length, value)

    def prepend(self, value):
        self.insert(0, value)

    def get_first(self):
        if self.__head:
            return self.__head
        return "Circular Doubly Linked List is empty"

    def get_index(self, value):
        if self.__head is None:
            raise ValueError("Circular Doubly Linked List is empty")
        
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
            raise TypeError(f"Circular Doubly Linked List only accepts elements of type {self.dataType}")
        temp_node = self.get_value(index)
        if temp_node:
            temp_node.value = value
            return True
        return False

    def delete_byIndex(self, index):
        if index < 0 or index >= self.__length:
            raise IndexError("Index out of bounds")
        if self.__length == 1:  # Only one node in the list
            deleted_node = self.__head
            self.__head = None
            self.__tail = None
        elif index == 0:  # Delete the head
            deleted_node = self.__head
            self.__head = self.__head.next
            self.__head.prev = self.__tail
            self.__tail.next = self.__head
        elif index == self.__length - 1:  # Delete the tail
            deleted_node = self.__tail
            self.__tail = self.__tail.prev
            self.__tail.next = self.__head
            self.__head.prev = self.__tail
        else:  # Delete in the middle
            temp_node = self.get_value(index - 1)
            deleted_node = temp_node.next
            temp_node.next = deleted_node.next
            deleted_node.next.prev = temp_node
        
        deleted_node.next = None
        deleted_node.prev = None
        self.__length -= 1
        return deleted_node

    def delete_byValue(self, value):
        index = self.get_index(value)
        return self.delete_byIndex(index)

def copy_CDLL(org_CDLL):
    new_CDLL = CircularDoublyLinkedList(org_CDLL.dataType)
    if org_CDLL.get_length() == 0:
        return new_CDLL
    
    current_node = org_CDLL.get_first()
    for _ in range(org_CDLL.get_length()):
        new_CDLL.append(current_node.value)
        current_node = current_node.next
    return new_CDLL
