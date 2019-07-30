"""Linear search implementation in python"""

# array does not have to be sorted

def linear_search(array: list, num: int)-> bool:
    num_in_list = [item for item in array if item == num]

    return True if num_in_list else False


print(linear_search([1,3,4,6,7,8], 5))
print(linear_search([1,3,4,6,7,8, 10], 10))
print(linear_search([ 2, 3, 4, 10, 40 ] , 11))