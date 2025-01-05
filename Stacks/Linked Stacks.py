class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedStack:
    def __init__(self,dataType = int):
        self.top = None
        self.dataType = dataType
        self.size = 0

    def __str__(self):
        current = self.top
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        return "\n↓\n".join(elements) if elements else "Stack is empty"
    
    def isEmpty(self):
        return self.size == 0
    
    def push(self, value):
        if not isinstance(value, self.dataType):
            raise TypeError(f"Stack only accepts elements of type {self.dataType}")
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        deleted_value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return deleted_value
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.top.value
    


ls = LinkedStack()
ls.push(1)
ls.push(2)
ls.push(3)
print(ls)
print()
ls.pop()
print(ls)