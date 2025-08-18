"""
Perform a linear search for a target value in an array.

Parameters:
arr (list): The list to search through.
target: The value to search for.

Returns:
int: The index of the target value if found, otherwise None.
"""

#Linear Search
def linear_Search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return None
                   
def verify(index):
   if index is not None:
       print("Result found at index: ", index)
   else:
       print('result is not found') 

number = [1,2,3,4,5,6,7,8,9,10]

result = linear_Search(number, 12)
verify(result)

result = linear_Search(number, 8)
verify(result)