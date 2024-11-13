class Array_1D:
    def __init__(self,capacity,dataType = int):
        self.capacity = capacity 
        self.array = [0] * capacity
        self.size = 0
        self.dataType = dataType
    
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
        
        if not isinstance(value,self.dataType):
            return "Array only accept elemnts of type int"
        
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
        
        for i in range(index,self.size-1):
            self.array[i] = self.array[i+1]
        
        self.array[self.size-1] = None
        self.size -= 1

    def display(self):
        print([self.array[i] for i in range(self.size)])

    
def get(arr, index):
    return arr.array[index]
def AccessElement(array,index):
    if index > len(array.array):
        index = len(array) - 1
    else:
        print(array.array[index])

def ArraySearch(array,target):
    for i in range(array.size):
        if array.array[i] == target:
            return i
    return "Element Not Found"

def ArraySort(array):
    if array.isEmpty():
        return "Array is Empty"
    sorted_array = sorted(array.array[:array.size])
    for i in range(array.size):
        array.array[i] = sorted_array[i]
    return "Array Sorted"

def ArrayTraverse(array):
    for i in array.array:
        print(i)

arr = Array_1D(5)
print(arr.insert(0,"s"))
arr.insert(1,11)
arr.insert(2,12)
arr.insert(8,22)
arr.insert(2,13)
arr.insert(2,14)
print(get(arr,3))

arr.display()