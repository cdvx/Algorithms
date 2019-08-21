"""Selection sort implementation in python"""

@profile
def selection_sort(l):
    for i in range(len(l)):
        min_i = i
        for j in range(i+1, len(l)):
            if l[min_i] > l[j]:
                min_i = j
        l[i], l[min_i] = l[min_i], l[i]
    return l


print(selection_sort([2,1,0,8,9,7,5]))   