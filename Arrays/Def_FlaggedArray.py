class FlaggedArray:
    def __init__(self, capacity):
        self.A = [None] * capacity  
        self.flag = [False] * capacity  
        self.capacity = capacity  
        self.size = 0  

    def is_full(self):
        return self.size == self.capacity  

    def is_empty(self):
        return self.size == 0 

    def insert(self, index, value):
        if 0 <= index < self.capacity:
            if not self.flag[index]:  
                self.size += 1  
            self.A[index] = value
            self.flag[index] = True  
        else:
            print("Index isout of bounds")

    def remove(self, index):
        if 0 <= index < self.capacity and self.flag[index]: 
            self.A[index] = None
            self.flag[index] = False  
            self.size -= 1  
        else:
            print("Index is either out of bounds or array is empty")  

    def print(self):
        print("Array:", self.A)
        print("Flags:", self.flag)

arr = FlaggedArray(10)

arr.insert(3, 50)
arr.insert(7, 61)    
arr.print()  

arr.remove(3)  
arr.print()  
