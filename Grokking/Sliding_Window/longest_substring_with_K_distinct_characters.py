# Given a string, 
# find the length of the longest substring in it
# with no more than K distinct characters.

# Example 1:
# Input: String="araaci", K=2
# Output: 4
# Explanation: 
# The longest substring 
# with no more than '2' distinct characters is "araa".

# Example 2:
# Input: String="araaci", K=1
# Output: 2
# Explanation:
# The longest substring 
# with no more than '1' distinct characters is "aa".

# Example 3:
# Input: String="cbbebi", K=3
# Output: 5
# Explanation: 
# The longest substrings 
# with no more than '3' distinct characters are "cbbeb" & "bbebi".


## Time complexity O(2N) >> O(N)
## space complexity O(K) as we will be storing K+1 characters 
## in hash map

import collections

def solution(str, k):
    window_start = 0 
    max_length = 0
    char_frequency = {} 

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_frequency: 
            ## can use collections.Counter() 
            ## to replace this if statement
            char_frequency[right_char] = 0 
        char_frequency[right_char] += 1 

        # shrink the sliding window, unitl we are left with 
        # k distinct characters in the char_frequency 
        while len(char_frequency) > k:
            left_char = str[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1 
        # remember max length so for
        max_length = max(max_length, 
                         window_end - window_start + 1)
    return max_length

def solution_2(str, k):
    window_start = 0 
    max_length = 0 
    char_frequency = collections.Counter()

    for window_end in range(len(str)):
        right_char = str[window_end]
        char_frequency[right_char] += 1
        ## shrink sliding window: if more letters than 
        ## allowed k 
        while len(char_frequency) > k:
            left_char = str[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1 ## shrink window
        max_length = max(max_length,
                         window_end - window_start + 1)
    return max_length

    

def main():
    print("Length of the longest substring: " + \
          str(solution("araaci", 2)))
    print("Length of the longest substring: " + \
          str(solution("araaci", 1)))
    print("Length of the longest substring: " + \
          str(solution("cbbebi", 3)))

def main_2():
    print("222 Length of the longest substring: " + \
          str(solution_2("araaci", 2)))
    print("222 Length of the longest substring: " + \
          str(solution_2("araaci", 1)))
    print("222 Length of the longest substring: " + \
          str(solution_2("cbbebi", 3)))

main()
main_2()
        