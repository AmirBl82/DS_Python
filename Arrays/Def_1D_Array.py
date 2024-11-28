class Array_1D:
    def __init__(self, capacity, dataType=int):  
        self.capacity = capacity
        self.array = [None] * capacity  
        self.size = 0
        self.dataType = dataType

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def insert(self, index, value):
        if not isinstance(value, self.dataType):
            raise TypeError(f"Array only accepts elements of type {self.dataType}") 
            
        if self.isFull():
            raise OverflowError("Array is Full")

        if index < 0 or index > self.size:  
            raise IndexError("Index out of Bounds")

        for i in range(self.size - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]

        self.array[index] = value
        self.size += 1

    def delete(self, index):
        if self.isEmpty():
            raise ValueError("Array is Empty")

        if index < 0 or index >= self.size:
            raise IndexError("Index out of Bounds")

        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]

        self.size -= 1  
        self.array[self.size] = None  

    def display(self):
        print([self.array[i] for i in range(self.size)])


def get(arr, index):
    if index < 0 or index >= arr.size:
        raise IndexError("Index out of Bounds")
    return arr.array[index]

def AccessElement(array, index):
    if index < 0 or index >= array.size:
        raise IndexError("Index out of Bounds")
    return array.array[index]

def ArraySearch(array, target):
    for i in range(array.size):
        if array.array[i] == target:
            return i
    return -1

def ArraySort(array):
    if array.isEmpty():
        raise ValueError("Array is Empty")
    sorted_array = sorted(array.array[:array.size])
    for i in range(array.size):
        array.array[i] = sorted_array[i]
    return "Array Sorted"

def ArrayTraverse(array):
    for i in range(array.size):
        print(array.array[i])

def ArrayReverse(array):
    if array.isEmpty():
        raise ValueError("Array is Empty")
    reversed_array = Array_1D(array.capacity, array.dataType)
    for i in range(array.size):
        reversed_array.insert(i, array.array[array.size - i - 1])
    return reversed_array

def Array_Divide(array1, array2):
    if array1.size != array2.size:
        raise ValueError("Arrays Sizes are not Equal to Divide")
    divided_array = Array_1D(array1.capacity, array1.dataType)
    for i in range(array1.size):
        if array2.array[i] == 0:
            raise ZeroDivisionError("Division by zero cannot be done")
        divided_array.insert(i, array1.array[i] // array2.array[i])
    return divided_array

def Array_Multiply(array1, array2):
    if array1.size != array2.size:
        raise ValueError("Arrays Sizes are not equal to Multiply")
    multiplied_array = Array_1D(array1.capacity, array1.dataType)
    for i in range(array1.size):
        multiplied_array.insert(i, array1.array[i] * array2.array[i])
    return multiplied_array

def Array_Pow(array1, array2):
    if array1.size != array2.size:
        raise ValueError("Arrays Sizes are not equal to Pow")
    pow_array = Array_1D(array1.capacity, array1.dataType)
    for i in range(array1.size):
        pow_array.insert(i, array1.array[i] ** array2.array[i])
    return pow_array


# Example usage
arr = Array_1D(7)
arr.insert(0, 1)
arr.insert(1, 11)
arr.insert(2, 12)
arr.insert(1, 22)
arr.insert(2, 13)
arr.insert(2, 14)
arr.display()
arr.delete(2)
print(get(arr, 3))
r_arr = ArrayReverse(arr)
arr.display()
r_arr.display()

arr1 = Array_1D(7)
arr1.insert(0, 1)
arr1.insert(1, 11)
arr1.insert(2, 12)
arr1.insert(1, 22)
arr1.insert(2, 13)
arr1.insert(2, 14)
divided_arr = Array_Divide(arr, arr1)
divided_arr.display()
multip_arr = Array_Multiply(arr, arr1)
multip_arr.display()
