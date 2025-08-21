s = "abcabcbb"
def lengthOfLongestSubstring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    :param s: Input string
    :return: Length of the longest substring without repeating characters
    """
    
    result = []
    max_length = 0
    for i in s:
        if i in result:
            dub = result.index(i)
            result = result[dub+1:]
        result.append(i)
        max_length = max(max_length, len(result))
    return max_length

print(lengthOfLongestSubstring(s))


