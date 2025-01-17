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
    

def del_odd(lstack):
    lstack1 = LinkedStack()
    current = lstack.top
    while current:
        if current.value % 2 == 0:
            lstack1.push(current.value)
        current = current.next
    for _ in range(lstack.size):
        lstack.pop()
    
    current1 = lstack1.top
    while current1:
        lstack.push(current1.value)
        current1 = current1.next
        lstack1.pop()


def del_odd(lstack):
    list = []
    current = lstack.top
    while current:
        if current.value % 2 == 0:
            list.append(current.value)
        current = current.next
    for _ in range(lstack.size):
        lstack.pop()
    
    while list:
        lstack.push(list.pop())
        
ls = LinkedStack()
ls.push(6)
ls.push(2)
ls.push(3)
ls.push(4)
print(ls)
print()
# ls.pop()
# print(ls)
del_odd(ls)
print(ls)

l = [1,2,3,4]
l.pop(2)
print(l)
