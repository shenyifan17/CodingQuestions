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
    char_index_map = collections.Counter() # record position 
    print(f'======================================= {str} ============================= ')

    ## try to extend the range [windowStart, windowEnd]
    for window_end in range(len(str)):
        right_char = str[window_end]
        print(f'window_end = {window_end}, right_char = {right_char}')
        # if the hash map alread contains right_char,
        # then shrink the window so that we only have 
        # one occurance of right_char
        if right_char in char_index_map:
            print(f'window_start = {window_start}, char_index_map = {char_index_map}, '\
                  f'char_index_map[right_char] + 1 = {char_index_map[right_char] + 1}')
            # in the current window, 
            # we will not have any right_char after its previous index
            # and if window_start is alread ahead of the last index of right_char
            # we will keep window_start 
            window_start = max(window_start, char_index_map[right_char]+1)
        # insert/update 'right_char' into the map
        print(f'insert/update {str[window_end]} to {window_end} ')
        char_index_map[str[window_end]] = window_end
        # remember the maximum length so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
  print("Length of the longest substring: " + str(solution("aabccbb")))
  print("Length of the longest substring: " + str(solution("abbbb")))
  print("Length of the longest substring: " + str(solution("aaabcdefghiigjlqpweoc")))
  print("Length of the longest substring: " + str(solution("asadqwezxxcvnkjsdffsdfg")))
  print("Length of the longest substring: " + str(solution("ae1234567asdasd33")))

main()
