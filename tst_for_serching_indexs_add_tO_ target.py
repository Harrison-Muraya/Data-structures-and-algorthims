
def soution(nums, target):

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print(f"Checking indices {i} and {j}: {nums[i]} + {nums[j]}")
            if nums[i] + nums[j] == target:
                return [i, j]

Nums = [2, 7, 11, 15]
Target = 26
result = soution(Nums, Target)
print(f"Indices of numbers that add up to {Target} are: {result}")