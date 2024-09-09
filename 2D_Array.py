import numpy as np
# Time Complexity for creating a 2D_Array is O(mn) where m is number of columns and n is number of rows
twoDArray = np.array([[1,2,3,4],[10,11,12,13],[20,21,22,23],[15,16,17,18]])
print(twoDArray)




# 2D_Array insertion Operation
# Time Complexity for 2D_Array insertion is O(mn) 
# If axis is 0 its going to add row but if axis is 1 its going to add column
new2DArray = np.insert(twoDArray, 0, [[99,98,97,96]], axis =0) 
print(new2DArray)
new2DArray = np.insert(twoDArray, 2, [[91,92,93,94]], axis =1) 
print(new2DArray)
new2DArray = np.append(twoDArray, [[77,78,79,80]], axis = 0)
print(new2DArray)
new2DArray = np.append(twoDArray, [[71],[72],[73],[74]], axis = 1)
print(new2DArray)



# Access 2D_Array Element(returns element of an index)
# Time Complexity of Accessing 2D_Array Element is O(1)
def AccessElement(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array):
        print("Incorrect index")
    else:
        print(array[rowIndex][colIndex])

AccessElement(twoDArray, 1, 10)



# 2D_Array Traversal Operation
# Time Complexity of Array Traversal is O(mn)

def Array_2DTraverse(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

Array_2DTraverse(twoDArray)



# Searching for 2D_Array Element(returns index of an element)
# Time Complexity of Searching for Array Element is O(n)

def Array2D_Search(array, target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == target:
                return i,j
    return "Element not found"

print(Array2D_Search(twoDArray,10))



#ِ Deleting a row or column from 2DArray
# Time Complexity for Deleting a row or column from 2DArray is O(mn)

new2D_Array = np.delete(twoDArray, 0, axis = 0)
new2D_Array = np.delete(twoDArray, 2 , axis = 1)

print(new2D_Array)

# Clearing a 2D_Array
# empty_array = twoDArray.reshape(0,0)

# Reversing a 2D_Array
reversed_rows_and_columns = twoDArray[::-1, ::-1]
print("Reversed Rows and Columns:\n", reversed_rows_and_columns)

# Slicing a 2D_Array

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print(arr[:2, :])
print(arr[:,:1])
print(arr[:, 1:3])

print(arr[:2, :2])

print(arr[2:, 2:])



# Sorting a 2D_Array
# In this for Sorting Row we use axis = 1 and column we use axis = 0

arr = np.array([
    [3, 2, 1],
    [9, 8, 7],
    [6, 5, 4]
])

# Step 2: Sort the 2D array by rows (sort each row individually)
sorted_by_rows = np.sort(arr, axis=1)

# Step 3: Sort the 2D array by columns (sort each column individually)
sorted_by_columns = np.sort(arr, axis=0)

# Print the results
print("Original array:")
print(arr)

print("\nArray sorted by rows:")
print(sorted_by_rows)

print("\nArray sorted by columns:")
print(sorted_by_columns)



# Finding Maximum Element of 2D_Array
arr12 = np.array([[1,2,3,4],[5,6,7,8],[14,17,18,33]])
max_value = np.max(arr12)
print(max_value)
