"""Binary search implementation in python"""

# precondition -> array has to be sorted

def binary_search(array: list, num: int)-> bool:
    list_len = len(array)
    half = lambda l: int(l/2)
    
    if num >= array[half(list_len)]:
        array = array[half(list_len):]
        list_len = len(array)
        
        return array[0] == num if list_len==1 else binary_search(array, num)
    else:
        array = array[:half(list_len)]
        list_len = len(array)

        return array[0] == num if list_len==1 else binary_search(array, num)


print(binary_search([1,3,4,6,7,8], 5))
print(binary_search([1,3,4,6,7,8, 10], 10))
print(binary_search([ 2, 3, 4, 10, 40 ] , 11))