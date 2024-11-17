# Time Complexity of Queue Creation is O(1)
class Queue:
    def __init__(self,maxSize,dataType):
        self.maxSize = maxSize
        self.__items = []
        self.__front = -1
        self.__rear = -1
        self.dataType = dataType
        
    
    def __str__(self):
        values = [str(x) for x in self.__items if x is not None]
        return ' '.join(values)
    
    # isEmpty
    # Time Complexity is O(1)
    def isEmpty(self):
        return self.__rear == self.__front
    
    # isFull
    # Time Complexity is O(1)
    def isFull(self):
        return self.__rear == self.maxSize - 1
    
    # Enqueue(Queue insert Method)
    # Time Complexity is O(1)
    def insert(self,value):
        if not isinstance(value, self.dataType):
            return f"Queue only accepts elements of type {self.dataType.__name__}"
            
        if self.isFull():
            return "The Queue is Full"
        else:
            self.__rear += 1
            self.__items.append(value)
            

    # Dequeue(Queue delete Method)
    # Time Complexity is O(1)
    def delete(self):
        if self.isEmpty():
            return "There is not any Element in the Queue"
        else:
            self.__front += 1
            return self.__items.pop(0)
    
    # Peek
    # Time Complexity is O(1)
    def peek(self):
        if self.isEmpty():
            return "There is not any Element in the Queue"
        else:
            return self.__items[0]
        
    
new_queue = Queue(4)
print(new_queue.isEmpty())
new_queue.insert(1)
new_queue.insert(2)
new_queue.insert(3)
new_queue.insert(4)
new_queue.insert(5)
new_queue.insert(6)
print(new_queue.insert(7))
print(new_queue)
print(new_queue.delete())
print(new_queue.delete())
print(new_queue)
print(new_queue.peek())
new_queue.delete()