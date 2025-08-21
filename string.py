def lengthOfLongestSubstring(s):

    """
    :type s: str
    :rtype: int
    """
    
    result = []
    for cha in s:
        if cha not in result:
            result.append(cha)
    print(f"Current result: {result}")
    return len(result)

s = "pwwkew"
result = lengthOfLongestSubstring(s)
# print(f"The length of the longest substring without repeating characters in '{s}' is: {result}")
print(result)