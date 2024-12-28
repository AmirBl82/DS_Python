class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None
    
class LinkedQueue:
    def __init__(self, dataType = int):
        self.front = None
        self.rear = None
        self.dataType = dataType
        self.size = 0
    
    def __str__(self):
        if self.isEmpty():
            return "Queue is Empty"
        
        elements = []
        current = self.front
        while current:
            elements.append(str(current.value))  
            current = current.next
        return " -> ".join(elements)   
        
    def isEmpty(self):
        return self.size == 0
    
    def insert(self, value):
        if not isinstance(value, self.dataType):
            raise TypeError(f"Queue only accepts elements of type {self.dataType}")
        new_node = Node(value)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
    
    def delete(self):
        if self.isEmpty():
            return "Queue is Empty"
        
        deleted_value = self.front.value
        self.front = self.front.next
        self.size -= 1
        return deleted_value
    
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.front.value
    

lq = LinkedQueue()
lq.insert(1)
lq.insert(2)
lq.insert(3)
lq.insert(4)
print(lq)  
print(lq.delete())
print(lq)
print(lq.peek())
