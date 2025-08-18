


"""
Perform binary search on a sorted array to find the index of the target value.

:param arr: List of sorted elements
:param target: Value to search for
:return: Index of target in arr if found, otherwise -1
"""
    # Binary search


def binary_search(arr, target):
    first = 0
    last = len(arr)-1
    
    while first <= last:
        midpoint = (first + last)// 2
        # print(f"{midpoint}, value of midpoint {arr[midpoint]}" )
        
        # Check if target is present at mid
        if arr[midpoint] == target:
            return midpoint
        # If target is greater, ignore left half
        elif arr[midpoint] < target:
            first = midpoint +1
            
        # If target is smaller, ignore right half
        else:
            first = midpoint -1
    return None

def verify(index):
    if index is not None:
        print("Result found at index: ", index)
    else:
        print('result is not found')    

number = [1,2,3,4,5,6,7,8,9,10]
result = binary_search(number, 12)  
verify(result)
result = binary_search(number, 8)   
verify(result)