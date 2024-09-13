# Time Complexity of Linear Search is O(n)
def linearSearch(list,value):
    for i in range(len(list)):
        if list[i] == value:
            return i
    return "Element does not exist"

# Time Complexity of Binary Search is O(logn)
def binarySearch(list, target):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == target:
            return mid  # Target found
        elif list[mid] < target:
            low = mid + 1  # Move to the right half
        else:
            high = mid - 1  # Move to the left half
    return "Element does not exist"


new_list = [20,40,30,50,90]
print(linearSearch(new_list,50))
print(linearSearch([20,40,30,50,90],100))
print(binarySearch(new_list,30))
print(binarySearch([20,40,30,50,90],130))