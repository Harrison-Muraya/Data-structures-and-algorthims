

def merge_sort(list):

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right =  merge_sort(right_half)

    return merge(left, right)

def split(list):
    mid = len(list)//2
    left_half = list[:mid]
    right_half = list[mid:]
    return left_half, right_half

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1