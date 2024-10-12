from array import *
# 'i' is type of Elements that we put in Array
my_array = array('i')               # Time Complexity of Storing is O(1)
print(my_array)
my_array1 = array('i', [1,2,3,4])   # Time Complexity of Storing is O(n)
print(my_array1)



# Array insertion Operation
# Time Complexity of Insertion into Array is O(n)
my_array2 = array('i', [1,2,3,4,5])
print(my_array2)
my_array2.insert(0,6)
print(my_array2) 
my_array2.insert(4,7)
print(my_array2)
my_array2.append(99)
print(my_array2)



# Array Extention(Merging)
MY_array = array('i',[10,20,30,40])
my_array2.extend(MY_array)
print(my_array2)
merged_array = MY_array + my_array2
print(my_array2)



# Adding items from list into array
List1 = [21,22,23]
my_array2.fromlist(List1)
print(my_array2)



# Array Traversal Operation
# Time Complexity of Array Traversal is O(n)
arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('f', [1.3,1.5,1.6])

def ArrayTraverse(array):
    for i in arr1:
        print(i)
ArrayTraverse(arr1)



# Access Array Element(returns element of an index)
# Time Complexity of Accessing Array Element is O(1)
Arr1 = array('i', [1,2,3,4,5,6])

def AccessElement(array, index):
    if index >= len(Arr1):
        print("There is not any element in this index")
    else:
        print(array[index])
AccessElement(Arr1, 5)



# Searching for Array Element(returns index of an element)
# Time Complexity of Searching for Array Element is O(n)
Arr2 = array('i', [1,2,3,4,5,6,7,8])

def Array_Search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return "Element Not Found"
print(Array_Search(Arr2, 7))



#ِ Deleting an Element from Array
# Time Complexity for Deleting an Element from Array is (If We Remove Last element its O(1)) O(n)
Arr3 = array('i', [1,2,3,4,5,6,7,8,9])

Arr3.remove(4)
print(Arr3)
del Arr3[2]
print(Arr3)
Arr3.pop()
print(Arr3)
# Clearing an Array
# Arr3[:] = array(Arr3.typecode)
print(Arr3)


# Finding an Elment index
print(Arr3.index(7))

# Reversing an arrray
Arr3.reverse()
print(Arr3)

# Get buffer information
print(Arr3.buffer_info())

# Checking number of occurrences of an array element
print(Arr3.count(5))

## Convert Array to list
print(Arr3.tolist())

#Slicing elements from array
print(Arr3[1:4])
print(Arr3[1:])
print(Arr3[:4])
print(Arr3[:]) 



# Sorting an Array
Arr11 = array('i', [9,5,3,1,8,10])
def ArraySort(arr):
    # Convert array to list
    list1 = arr.tolist()
    # Sort the list
    list1.sort()
    # Convert sorted list back to array
    sorted_array = array(arr.typecode, list1)
    return sorted_array

sorted_Arr11 = ArraySort(Arr11)
print("Sorted Arr11:", sorted_Arr11)


# Finding Maximum Element of array
arr12 = array('i', [25,5,10,16,17])
max_value = max(arr12)
print(max_value)

# Element Assignment
arr12[2] = 20
print(arr12)
