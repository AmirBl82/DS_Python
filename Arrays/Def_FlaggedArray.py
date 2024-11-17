class FlaggedArray:
    def __init__(self, capacity):
        self.array = [None] * capacity  
        self.flag = [False] * capacity  
        self.capacity = capacity  
        self.size = 0  

    def is_full(self):
        return self.size == self.capacity  

    def is_empty(self):
        return self.size == 0 

    def insert(self, index, value):
        if index < 0 or index >= self.capacity:
            return "Index Out Of Bounds!"
        
        if self.is_full():
            return "The Array is Full!"
    
        if not self.flag[index]:
            self.array[index] = value
            self.flag[index] = True
            self.size += 1
        else:
            for i in range(self.capacity - 1, index, -1):
                if self.flag[i - 1]:
                    self.array[i] = self.array[i - 1]
                    self.flag[i] = self.flag[i - 1]
        self.array[index] = value
        self.flag[index] = True
        self.size += 1


    def remove(self, index):
        if 0 <= index < self.capacity and self.flag[index]: 
            self.array[index] = None
            self.flag[index] = False  
            self.size -= 1  
        else:
            print("Index is either out of bounds or array is empty")  

    def print(self):
        print("Array:", self.array)
        print("Flags:", self.flag)

arr = FlaggedArray(10)

arr.insert(3, 50)
arr.insert(7, 61)    
arr.insert(7, 62)  
arr.print()  

arr.remove(3)  
arr.print()  

l = [2]
l.append(2)
print(l)