"""Insertion sort implementation"""

def insertion_sort(l):
    for index in range(1,len(l)):

        currentvalue = l[index]
        position = index
        while position>0 and l[position-1]>currentvalue:
            l[position] = l[position-1]
            position = position-1

        l[position]=currentvalue
    return l

print(insertion_sort([4,5,2,6,3,1]))