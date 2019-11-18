# Problem Statement
# Given a string, 
# find the length of the longest substring 
# which has no repeating characters.
# 
# Example 1:
# Input: String="aabccbb"
# Output: 3
# Explanation: 
# The longest substring without any repeating characters is "abc".

# Example 2:
# Input: String="abbbb"
# Output: 2
# Explanation: 
# The longest substring without any repeating characters is "ab".

# Example 3:
# Input: String="abccde"
# Output: 3
# Explanation: 
# Longest substrings without any repeating characters are "abc" & "cde".

import collections 

def solution(str):
    """"
    This problem follows the Sliding Window 
    pattern and we can use a similar 
    dynamic sliding window strategy 
    as discussed in 
    Longest Substring with K Distinct Characters. 
    We can use a HashMap to remember 
    the last index of each character we have processed. 
    Whenever we get a repeating character 
    we will shrink our sliding window 
    to ensure that we always have 
    distinct characters in the sliding window.
    """
    window_start = 0 
    max_length = 0
    char_index_map = collections.Counter()

    ## try to extend the range [windowStart, windowEnd]
    for window_end in range(len(str)):
        right_char = str[window_end]



