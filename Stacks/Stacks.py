# Time Complexity of Stack Creation is O(1)
class Stack:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.__list = []
        self.__top = -1
    
    def __str__(self):
        values = [str(x) for x in reversed(self.__list)]
        return '\n'.join(values)
    
    # isEmpty
    # Time Complexity is O(1)
    def isEmpty(self):
        return self.__top == -1
    
    # isFull
    # Time Complexity is O(1)
    def isFull(self):
        return self.__top == self.maxSize - 1
    
    # Push
    # Time Complexity is O(1)
    def push(self,value):
        if self.isFull():
            return "The Stack is Full"
        else:
            self.__list.append(value)
            self.__top += 1
    
    # Pop
    # Time Complexity is O(1)
    def pop(self):
        if self.isEmpty():
            return "The Stack is Empty"
        else:
            self.__top -= 1
            return self.__list.pop()
            
    
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
    
    # # getSize
    # # Time Complexity is O(1)
    # def getSize(self):
    #     return len(self.__list)
    
    # # Find Max
    # # Time Complexity is O(n)
    # def findMax(self):
    #     if self.isEmpty():
    #         return "The Stack is Empty"
    #     else:
    #         return max(self.__list)
        
def copy_stack(org_stack):
    temp_stack = Stack(org_stack.maxSize)
    copy_stack = Stack(org_stack.maxSize)
    while not org_stack.isEmpty():
        temp_stack.push(org_stack.pop())    
        
    while not temp_stack.isEmpty():
        value = temp_stack.pop()
        org_stack.push(value)
        copy_stack.push(value)
    return copy_stack

def merge(stack1, stack2):
    stack1_copy = copy_stack(stack1)
    stack2_copy = copy_stack(stack2)

    merged_stack = Stack(stack1_copy.maxSize + stack2_copy.maxSize)

    while not stack1_copy.isEmpty() or not stack2_copy.isEmpty():
        if stack1_copy.isEmpty():
            merged_stack.push(stack2_copy.pop())
        elif stack2_copy.isEmpty():
            merged_stack.push(stack1_copy.pop())
        else:
            if stack1_copy.peek() > stack2_copy.peek():
                merged_stack.push(stack1_copy.pop())
            else:
                merged_stack.push(stack2_copy.pop())

    reversed_stack = Stack(merged_stack.maxSize)
    while not merged_stack.isEmpty():
        reversed_stack.push(merged_stack.pop())

    return reversed_stack


def findMax(stack):
    if stack.isEmpty():
        return "The Stack is Empty"
    
    max_value = stack.peek()
    temp_stack = Stack(stack.maxSize)
    
    while not stack.isEmpty():
        value = stack.pop()
        if value > max_value:
            max_value = value
        temp_stack.push(value)
    
    while not temp_stack.isEmpty():
        stack.push(temp_stack.pop())
    return max_value


new_stack = Stack(4)

print(new_stack.isEmpty())        
print(new_stack.isFull())
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
# new_stack.pop()
# # new_stack.delete()
# print(new_stack)
# print(new_stack.getSize())
print(findMax(new_stack))
# print(new_stack)

stack1 = Stack(4)
stack2 = Stack(4)
stack1.push(1)
stack1.push(2)
stack1.push(2)
stack1.push(4)
stack2.push(10)
stack2.push(12)
stack2.push(20)
stack2.push(30)
print(merge(stack1,stack2))
print(stack1)
print(stack2)

