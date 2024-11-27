# Time Complexity of Circular Queue Creation is O(1)
class CircularQueue:
    def __init__(self, maxSize,dataType = int):
        self.maxSize = maxSize
        self.__items = [None] * maxSize
        self.__front = -1
        self.__rear = -1
        self.dataType = dataType

    def __str__(self):
        values = [str(x) for x in self.__items if x is not None]
        return ' '.join(values)

    # isFull
    # Time Complexity is O(1)
    def isFull(self):
        return (self.__rear+1) % self.maxSize == self.__front

    # isEmpty
    # Time Complexity is O(1)
    def isEmpty(self):
        return self.__front == self.__rear

    # Enqueue (Queue append Method)
    # Time Complexity is O(1)
    def insert(self, value):
        if not isinstance(value, self.dataType):
            raise TypeError(f"Queue only accepts elements of type {self.dataType}") 
            
        if self.isFull():
            raise OverflowError("Queue is Full")
        self.__rear = (self.__rear + 1) % self.maxSize
        self.__items[self.__rear] = value

    # Dequeue (Queue pop Method)
    # Time Complexity is O(1)
    def delete(self):
        if self.isEmpty():
            return "There is not any Element in the Queue"
        else:
            self.__front = (self.__front + 1) % self.maxSize
            x = self.__items[self.__front]
            self.__items[self.__front] = None
            return x

    # Peek
    # Time Complexity is O(1)
    def peek(self):
        if self.isEmpty():
            return "There is not any Element in the Queue"
        else:
            return self.__items[self.__front + 1]

    # Delete
    # Time Complexity is O(1)



new_circqueue = CircularQueue(3)
print(new_circqueue.isFull())
print(new_circqueue.isEmpty())
new_circqueue.insert(1)
new_circqueue.insert(2)
new_circqueue.insert(3)
print(new_circqueue)
print(new_circqueue.delete())
# print(new_circqueue.delete())
# print(new_circqueue.delete())
print(new_circqueue)
print(new_circqueue.peek())