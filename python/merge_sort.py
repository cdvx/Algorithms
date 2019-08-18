"""Merge Sort implementation python"""

split = lambda l: (l[:(len(l)//2)], l[(len(l)//2):])

def merge_sort(arr):
    if len(arr) <=1:
        return arr
    else:
        left, right = split(arr)
        return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    i_left = i_right = 0

    target = len(left) + len(right)

    merged = []

    while len(merged) < target:
        if left[i_left] <= right[i_right]:
            merged.append(left[i_left])
            i_left += 1
        else:
            merged.append(right[i_right])
            i_right += 1
        
        if i_right == len(right):
            merged += left[i_left:]
            break
        elif i_left == len(left):
            merged += right[i_right:]
            break
    return merged


print(merge_sort([4,3,7,4,1]))