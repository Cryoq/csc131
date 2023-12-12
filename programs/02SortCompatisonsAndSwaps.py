###################################################################################
# Name: Alan Dreher
# Date: December 10 2023
# Description: Sorts lists using bubble, optimized bubble, selection, and insertion
#              and calculates the number of comparisons and swaps
###################################################################################


# Creates the list
def getList():
#    return [100,5,63,29,69,74,96,80,82,12]
#    return [82, 65, 93, 0, 60, 31, 99, 90, 31, 70]
    return [63, 16, 78, 69, 36, 36, 3, 66, 75, 100]
#    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#    return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#    return [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]

# The bubble sort function
def bubbleSort(arr = list[int]):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n-1):
        
        for j in range(n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                swaps += 1
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print(f"After bubble sort: {arr}")
    return comparisons, swaps

#The optimizes bubble sort funciton
def optBubbleSort(arr = list[int]):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n-1):
        changed = False
        
        for j in range(n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                changed = True
                swaps += 1
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        if not changed:
            break
    print(f"After optimised bubble sort: {arr}")
    return comparisons, swaps

# The selection sort function
def selectionSort(arr = list[int]):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n-1):
        min_index = i
        
        for j in range(i+1,n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        swaps += 1
        arr[i], arr[min_index] = arr[min_index], arr[i]

    print(f"After selection sort: {arr}")
    return comparisons, swaps

# The insertion sort function
def insertionSort(arr = list[int]):
    n = len(arr)
    comparisons = 0
    swaps = 0
    print(arr)
    
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        comparisons += 2
        while j >= 0 and arr[j] >= temp:
            if arr[j] == temp:
                comparisons -= 3
            comparisons += 1
            swaps += 1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
        
    print(f"After insertion sort: {arr}")
    return comparisons, swaps

def compAndSwaps(comparisons, swaps):
    print(f"{comparisons} comparisons; {swaps} swaps")


# -------------------- MAIN --------------------
bubbleComp, bubbleSwaps = bubbleSort(getList())
compAndSwaps(bubbleComp, bubbleSwaps)

optBubbleComp, optBubbleSwaps = optBubbleSort(getList()) 
compAndSwaps(optBubbleComp, optBubbleSwaps)

selectionComp, selectionSwap = selectionSort(getList())
compAndSwaps(selectionComp, selectionSwap)

inserstionComp, insertionSwaps = insertionSort(getList())
compAndSwaps(inserstionComp, insertionSwaps)