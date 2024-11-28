class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, dataType=int):
        self.__head = None  # Private head
        self.length = 0
        self.dataType = dataType

    def __str__(self):
        temp_node = self.__head
        result = ""
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result

    # Insert an element at a specific index
    def insert(self, index, value):
        if not isinstance(value, self.dataType):
            raise TypeError(f"Linked List only accepts elements of type {self.dataType}") 
        
        if index < 0 or index > self.length:
            raise IndexError("Index out of Bounds")
        new_node = Node(value)

        if index == 0:  # Insert at the beginning
            new_node.next = self.__head
            self.__head = new_node
        else:
            temp_node = self.__head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node

        self.length += 1
    
    def append(self,value):
        self.insert(self.length,value)
    
    def prepend(self,value):
        self.insert(0,value)

    # Remove an element at a specific index
    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of Range") 

        if index == 0:  # Remove the first element
            removed_node = self.__head
            self.__head = self.__head.next
        else:
            prev_node = self.get_value(index - 1)
            removed_node = prev_node.next
            prev_node.next = removed_node.next

        removed_node.next = None
        self.length -= 1
        return removed_node

    # Traverse the linked list
    def traverse(self):
        current_node = self.__head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    # Get the node at a specific index
    def get_value(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of Range") 
        current_node = self.__head
        for _ in range(index):
            current_node = current_node.next
        return current_node
    
    # Get node address by value
    def get_address(self, value):
        current_node = self.__head
        while current_node:
            if current_node.value == value:
                return current_node  # Return the node itself (reference to the node)
            current_node = current_node.next
        raise ValueError("The Element does not exist")

    # Update the value of a node at a specific index
    def set_value(self, index, value):
        temp_node = self.get_value(index)
        if temp_node:
            temp_node.value = value
            return True
        return False

    # Delete all nodes in the linked list
    def delete_all(self):
        self.__head = None
        self.length = 0

    # Get the head
    def get_first(self):
        if self.__head:
            return self.__head
        return "Linked List is Empty"

    def get_index(self, value):
        current_node = self.__head
        index = 0
        while current_node:
            if current_node.value == value:
                return index
            current_node = current_node.next
            index += 1
        raise ValueError("The element does not exist")


linked_list = LinkedList()
linked_list.insert(0, 10)
linked_list.insert(1, 20)

node = linked_list.get_address(10)
node1 = linked_list.get_address(20)
index = linked_list.get_value(0)
first_node = linked_list.get_first()

print(id(node))
print(id(node1))
print(index.value)
print(first_node.value)



