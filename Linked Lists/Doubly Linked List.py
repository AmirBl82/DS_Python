class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, dataType=int):
        self.__head = None
        self.length = 0
        self.dataType = dataType

    def __str__(self):
        temp_node = self.__head
        result = ""
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " <-> "
            temp_node = temp_node.next
        return result

    def insert(self, index, value):
        if not isinstance(value, self.dataType):
            raise TypeError(f"Doubly Linked List only accepts elements of type {self.dataType}")
        if index < 0 or index > self.length:
            raise IndexError("Index out of Bounds")
        new_node = Node(value)
        if index == 0:
            new_node.next = self.__head
            if self.__head:
                self.__head.prev = new_node
            self.__head = new_node
        else:
            temp_node = self.__head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            new_node.prev = temp_node
            if temp_node.next:
                temp_node.next.prev = new_node
            temp_node.next = new_node
        self.length += 1

    def append(self, value):
        self.insert(self.length, value)

    def prepend(self, value):
        self.insert(0, value)

    def get_first(self):
        return self.__head if self.__head else "Doubly Linked List is Empty"

    def get_index(self, value):
        current_node = self.__head
        index = 0
        while current_node:
            if current_node.value == value:
                return index
            current_node = current_node.next
            index += 1
        raise ValueError("Element does not exist")

    def get_value(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        current_node = self.__head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def get_address(self, value):
        current_node = self.__head
        while current_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.next
        raise ValueError("Element does not exist")

    def set_value(self, index, value):
        temp_node = self.get_value(index)
        if temp_node:
            temp_node.value = value
            return True
        return False

    def delete_byIndex(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        if index == 0:
            deleted_node = self.__head
            self.__head = self.__head.next
            if self.__head:
                self.__head.prev = None
        else:
            prev_node = self.get_value(index - 1)
            deleted_node = prev_node.next
            prev_node.next = deleted_node.next
            if deleted_node.next:
                deleted_node.next.prev = prev_node
        deleted_node.next = None
        deleted_node.prev = None
        self.length -= 1
        return deleted_node

    def delete_byAddress(self, deleted_node):
        if deleted_node is None:
            raise ValueError("Value cannot be None")
        self.get_address(deleted_node.value)
        if self.__head == deleted_node:
            self.__head = self.__head.next
            if self.__head:
                self.__head.prev = None
        else:
            prev_node = self.__head
            while prev_node and prev_node.next != deleted_node:
                prev_node = prev_node.next
            if prev_node:
                prev_node.next = deleted_node.next
                if deleted_node.next:
                    deleted_node.next.prev = prev_node
        deleted_node.next = None
        deleted_node.prev = None
        self.length -= 1
        return deleted_node

    def delete_all(self):
        self.__head = None
        self.length = 0

    def traverse(self):
        current_node = self.__head
        while current_node:
            print(current_node.value)
            current_node = current_node.next