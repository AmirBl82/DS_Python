class PriorityQueue:
    def __init__(self,maxSize,dataType = int):
        self.maxSize = maxSize
        self.__list = []
        self.__front = -1
        self.__rear = -1
        self.dataType = dataType
    
    def __str__(self):
        values = [str(x) for x in self.__list if x is not None]
        return ' '.join(values)
    
    def isEmpty(self):
        return self.__front == self.__rear
    
    def isFull(self):
        return self.__rear == self.maxSize - 1
    
    def insert(self,value,priority):
        if not isinstance(value, self.dataType):
            raise TypeError(f"Queue only accepts elements of type {self.dataType}")     
        
        if self.isFull():
            raise OverflowError("The Queue is Full")
        self.__rear = (self.__rear + 1) % self.maxSize
        self.__list.append([value,priority])
        self.__list.sort(key = lambda x:x[1])

    def delete(self):
        if self.isEmpty():
            return "Queue is empty"
        self.__front = (self.__front + 1) % self.maxSize
        x = self.__list[self.__front]
        self.__list[self.__front] = None
        return x
    
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.__list[self.__front + 1]


new_queue = PriorityQueue(6)
print(new_queue.isEmpty())
new_queue.insert(71,8)
new_queue.insert(90,3)
new_queue.insert(14,2)
new_queue.insert(19,9)
new_queue.insert(18,5)
new_queue.insert(11,6)
print(new_queue)
print(new_queue.delete())
print(new_queue)
print(new_queue.peek())