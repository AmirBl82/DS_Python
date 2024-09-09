# Time Complexity of Queue Creation is O(1)
class Queue:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.__items = []
    
    def __str__(self):
        values = [str(x) for x in self.__items]
        return ' '.join(values)
    
    # isEmpty
    # Time Complexity is O(1)
    def isEmpty(self):
        if self.__items == []:
            return True
        else:
            return False
    
    # isFull
    # Time Complexity is O(1)
    def isFull(self):
        if len(self.__items) == self.maxSize:
            return True
        else:
            return False
    
    # Enqueue(Queue append Method)
    # Time Complexity is O(1)
    def enqueue(self,value):
        if self.isFull():
            return "The Queue is Full"
        else:
            self.__items.append(value)
            return "The Element is inserted at the End of Queue"
    
    # Dequeue(Queue pop Method)
    # Time Complexity is O(1)
    def dequeue(self):
        if self.isEmpty():
            return "There is not any Element in the Queue"
        else:
            return self.__items.pop(0)
    
    # Peek
    # Time Complexity is O(1)
    def peek(self):
        if self.isEmpty():
            return "There is not any Element in the Queue"
        else:
            return self.__items[0]
        
    # Delete
    # Time Complexity is O(1)
    def delete(self):
        self.__items = None
    
new_queue = Queue(4)
print(new_queue.isEmpty())
new_queue.enqueue(1)
new_queue.enqueue(2)
new_queue.enqueue(3)
new_queue.enqueue(4)
new_queue.enqueue(5)
new_queue.enqueue(6)
print(new_queue.enqueue(7))
print(new_queue)
new_queue.dequeue()
new_queue.dequeue()
print(new_queue)
print(new_queue.peek())
new_queue.delete()