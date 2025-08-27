def linear_search(arr, target):
    for i in range(0,len(arr)):
        if arr[i] == target:
            return i
    return None

def binary_search(arr, target):
    first = 0
    last = len(arr)-1
    
    while first <= last:
        midpoint = (first + last)//2
        if arr[midpoint] == target:
            return midpoint 
        elif arr[midpoint] < target:
            print(midpoint)
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print("Found at index: ", index)
    else:
        print("value not found")

nums = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(nums,12)
#verify(result)


def recursive_binary_search(arr, target):
    if len(arr) == 0:
        return False
    else:
        midpoint = len(arr)//2
        if arr[midpoint] == target:
            return True
        elif arr[midpoint] < target:
            return recursive_binary_search(arr[midpoint+1:], target)
        elif arr[midpoint] > target:
            return recursive_binary_search(arr[:midpoint-1], target)


def verify(index):
    if index is not False:
        print("Found ",)
    else:
        print("value not found")

nums = [1,2,3,4,5,6,7,8,9,10]

result = recursive_binary_search(nums,12)
print(result)
verify(result)
