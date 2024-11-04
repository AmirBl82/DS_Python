# Time Complexity of Circular Queue Creation is O(1)
class CircularQueue:
    def __init__(self, maxSize):
        self.__items = maxSize * [None]
        self.maxSize = maxSize
        self.__front = -1
        self.__rear = -1

    def __str__(self):
        values = [str(x) for x in self.__items]
        return ' '.join(values)

    # isFull
    # Time Complexity is O(1)
    def isFull(self):
        if self.__rear + 1 == self.__front:
            return True
        elif self.__front == 0 and self.__rear + 1 == self.maxSize:
            return True
        else:
            return False

    # isEmpty
    # Time Complexity is O(1)
    def isEmpty(self):
        if self.__rear == -1:
            return True
        else:
            return False

    # Enqueue (Queue append Method)
    # Time Complexity is O(1)
    def enqueue(self, value):
        if self.isFull():
            return "The Queue is Full"
        else:
            if self.__rear + 1 == self.maxSize:
                self.__rear = 0
            else:
                self.__rear += 1
                if self.__front == -1:
                    self.__front = 0
            self.__items[self.__rear] = value
            return "The element is inserted at the end of queue"

    # Dequeue (Queue pop Method)
    # Time Complexity is O(1)
    def dequeue(self):
        if self.isEmpty():
            return "There is not any Element in the Queue"
        else:
            firstElement = self.__items[self.__front]
            front = self.__front
            if self.__front == self.__rear:
                self.__front = -1
                self.__rear = -1
            elif self.__front + 1 == self.maxSize:
                self.__front = 0
            else:
                self.__front += 1
            self.__items[front] = None
            return firstElement

    # Peek
    # Time Complexity is O(1)
    def peek(self):
        if self.isEmpty():
            return "There is not any Element in the Queue"
        else:
            return self.__items[self.__front]

    # Delete
    # Time Complexity is O(1)
    def delete(self):
        self.__items = self.maxSize * [None]
        self.__rear = -1
        self.__front = -1


new_circqueue = CircularQueue(3)
print(new_circqueue.isFull())
print(new_circqueue.isEmpty())
new_circqueue.enqueue(1)
new_circqueue.enqueue(2)
new_circqueue.enqueue(3)
print(new_circqueue)
print(new_circqueue.enqueue(4))
new_circqueue.dequeue()
new_circqueue.dequeue()
print(new_circqueue.peek())