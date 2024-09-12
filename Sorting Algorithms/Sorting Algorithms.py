# Time Comploexity of Bubble Sort is O(n^2)
def bubbleSort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    print(list)

# Time Complexity of Selection Sort is O(n^2)
def selectionSort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i], list[min_index] = list[min_index] , list[i]
    print(list)

# Time Complexity of insertion Sort is O(n^2)
def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    print(list)

# Time Complexity of Merge function is O(n)
def merge(list, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = list[left + i]
    
    for j in range(0 ,n2):
        R[j] = list[mid + 1 + j]
    
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j +=1
        k += 1
    while i < n1:
        list[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        list[k] = R[j]
        j += 1
        k += 1

# Time Complexity of Merge Sort is O(nlogn)        
def mergeSort(list, left, right):
    if left < right:
        mid = (left+(right-1))//2
        mergeSort(list, left, mid)
        mergeSort(list, mid+1, right)
        merge(list, left, mid, right)
    return list

# Time Complexity of Quick Sort is O(nlogn)
def quickSort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]  
        left = [x for x in list if x < pivot]
        middle = [x for x in list if x == pivot]
        right = [x for x in list if x > pivot]
        return quickSort(left) + middle + quickSort(right)





    





new_list = [6,1,4,9,8,2,3,5,7,6]
bubbleSort(new_list)
bubbleSort([1,4,3,2,5,7,6,9,8,10])
selectionSort(new_list)
selectionSort([1,4,3,2,5,7,6,9,8,10])
insertionSort(new_list)
insertionSort([1,4,3,2,5,7,6,9,8,10])
print(mergeSort(new_list, 0, 8))
sorted_list = quickSort(new_list)
print(new_list)
print(quickSort(new_list))