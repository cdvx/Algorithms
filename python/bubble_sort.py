"""Bubble sort implementation in python"""

def swap(arr, x,y):
    arr[x], arr[y] = (arr[y], arr[x])
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            next_ = j if (j +1) == n else j + 1
            arr = swap(arr,j,next_) if arr[j] > arr[next_] else arr
    return arr


print(bubble_sort([4,5,2,6,3,1]))