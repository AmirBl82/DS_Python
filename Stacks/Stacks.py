# Time Complexity of Stack Creation is O(1)
class Stack:
    def __init__(self,maxSize,top):
        self.maxSize = maxSize
        self.__list = []
        self.__top = -1
    
    def __str__(self):
        values = self.__list.reverse()
        values = [str(x) for x in self.__list]
        return '\n'.join(values)
    
    # isEmpty
    # Time Complexity is O(1)
    def isEmpty(self):
        if self.__list == []:
            return True
        else:
            return False
    
    # isFull
    # Time Complexity is O(1)
    def isFull(self):
        if len(self.__list) == self.maxSize:
            return True
        else:
            return False
    
    # Push
    # Time Complexity is O(1)
    def push(self,value):
        if self.isFull():
            return "The Stack is Full"
        else:
            self.__list.append(value)
            self.__top += 1
            return "The Element has been successfully inserted"
    
    # Pop
    # Time Complexity is O(1)
    def pop(self):
        if self.isEmpty():
            return "There is not any Element in the Stack"
        else:
            return self.__list.pop()
            self.__top -= 1
    
    # Peek
    # Time Complexity is O(1)
    def peek(self):
        if self.isEmpty():
            return "There is not any Elemnet in the Stack"
        else:
            return self.__list[-1]
    
    # Delete
    # Time Complexity is O(1)
    def delete(self):
        self.__list = None
    
    # getSize
    # Time Complexity is O(1)
    def getSize(self):
        return len(self.__list)
    
    # Find Max
    # Time Complexity is O(n)
    def findMax(self):
        if self.isEmpty():
            return "The Stack is Empty"
        else:
            return max(self.__list)
        

new_stack = Stack(4)
print(new_stack.isEmpty())        
print(new_stack.isFull())
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
new_stack.pop()
# new_stack.delete()
print(new_stack)
print(new_stack.getSize())


        

