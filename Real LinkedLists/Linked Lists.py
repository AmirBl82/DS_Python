class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class LinkedList:
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
                result += " -> "
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
    
    def append(self,value):
        if not isinstance(value, self.dataType):
            raise TypeError(f"Linked List only accepts elements of type {self.dataType}")

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.length += 1
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        self.length += 1
    
    def delete(self, deleted_node):
        if deleted_node is None:
            raise ValueError("Cannot delete a Null Node")
        
        if self.head == deleted_node:
            self.head = self.head.next
            self.length -= 1
            return
        current_node = self.head
        while current_node.next:
            if current_node.next == deleted_node:
                 current_node.next = current_node.next.next
                 self.length -= 1
                 return
            current_node = current_node.next
        raise ValueError("Node not found")


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print(ll)
node = ll.head.next
ll.delete(node)
print(ll)
print(node)
print(ll.length)