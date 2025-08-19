
"""
Perform a recursive binary search on a sorted array to find the index of the target value.

:param arr: List of sorted elements
:param target: Value to search for
:return: Index of target in arr if found, otherwise -1
"""



def recusive_binary_Search(arry, target):

    if len(arry) == 0:
        return False
    else:
        midpoint = len(arry) // 2
        
        # Check if target is present at mid
        if arry[midpoint] == target:
            return midpoint
        
        # If target is greater, ignore left half
        elif arry[midpoint] < target:
            return recusive_binary_Search(arry[midpoint + 1:], target)
        
        # If target is smaller, ignore right half
        else:
            return recusive_binary_Search(arry[:midpoint], target)
        
def verify(index):
    if index is not False:
        print("Result found ", )
    else:
        print('result is not found')

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = recusive_binary_Search(number, 10)
verify(result)