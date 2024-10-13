class Array_1D:
    def __init__(self,capacity):
        self.capacity = capacity 
        self.array = [0] * capacity
        self.size = 0
    
    def isFull(self):
        return self.size == self.capacity
               
    def isEmpty(self):
        return self.size == 0
    
    def insert(self,index,value):
        if self.isFull():
            return "Array is Full,Cannot insert."
        
        if index < 0:
            index = self.size + index + 1
        
        if index > self.size:
            index = self.size
        
        for i in range(self.size-1,index-1,-1):
            self.array[i+1] = self.array[i]
        
        self.array[index] = value
        self.size +=1

    def delete(self,index):
        if self.isEmpty():
            return "Array is Empty"

        if index < 0:
            index = self.size + index + 1
        
        if index > self.size:
            index = self.size
        
        for i in range(index,self.size):
            self.array[i-1] = self.array[i]
        
        self.array[self.size-1] = None
        self.size -= 1

    def display(self):
        print([self.array[i] for i in range(self.size)])

    
arr = Array_1D(5)
arr.insert(0,10)
arr.insert(1,11)
arr.insert(2,12)
arr.insert(1,22)
arr.insert(-1,17)
arr.delete(-1)
arr.display()
print(arr.isFull())