class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result

    # Insert an element at a specific index
    # Time Complexity is O(n)
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0:
            index = self.length + index + 1
        if index < 0 or index > self.length:
            return False  # Invalid index

        if index == 0:  # Insert at the beginning
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node

        self.length += 1
        return True

    # Remove an element at a specific index
    # Time Complexity is O(n)
    def remove(self, index):
        if index < 0:
            index = self.length + index
        if index < 0 or index >= self.length:
            return False  # Invalid index

        if index == 0:  # Remove the first element
            removed_node = self.head
            self.head = self.head.next
        else:
            prev_node = self.get(index - 1)
            removed_node = prev_node.next
            prev_node.next = removed_node.next

        removed_node.next = None
        self.length -= 1
        return removed_node

    # Traverse the linked list
    # Time Complexity is O(n)
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    # Search for an element in the linked list
    # Time Complexity is O(n)
    def search(self, target):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == target:
                return index
            current_node = current_node.next
            index += 1
        return "This Element Does not exist"

    # Get the node at a specific index
    # Time Complexity is O(n)
    def get(self, index):
        if index < 0:
            index = self.length + index
        if index < 0 or index >= self.length:
            return None
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    # Update the value of a node at a specific index
    # Time Complexity is O(n)
    def set_value(self, index, value):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False

    # Delete all nodes in the linked list
    # Time Complexity is O(1)
    def delete_all(self):
        self.head = None
        self.length = 0

