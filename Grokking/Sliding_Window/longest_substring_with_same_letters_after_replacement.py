# Problem Statement
# Given a string with lowercase letters only, 
# if you are allowed to replace no more than 
# ‘k’ letters with any letter, 
# find the length of the longest substring 
# having the same letters after replacement.

# Example 1:
# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

# Example 2:
# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

# Example 3:
# Input: String="abccde", k=1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

import collections 

def length_of_longest_substring(str, k):
    """"
    This problem follows the Sliding Window pattern 
    and we can use a similar dynamic sliding window strategy 
    as discussed in No-repeat Substring. 
    We can use a HashMap to count the frequency of each letter.

    We’ll iterate through the string to add one letter 
    at a time in the window. 
    We’ll also keep track of the count of the 
    maximum repeating letter in any window 
    (let’s call it maxRepeatLetterCount). 
    So at any time, we know that we can have a window 
    which has one letter repeating maxRepeatLetterCount times, 
    this means we should try to replace the remaining letters. 
    If we have more than ‘k’ remaining letters, 
    we should shrink the window as 
    we are not allowed to replace more than ‘k’ letters.

    Time Complexity: O(N) where N is the number of letters in the input string
    Space Conmplexity: O(K), but as we limit to lower case letters,
                             we conclude it to be O(26) >> O(1)
    """
    window_start = 0
    max_length = 0 
    max_repeat_letter_count = 0  ## for a window
    frequency_map = collections.Counter()
    print(f'================= {str} ===============')
     
    # Extend the range [window_start, window_end]
    for window_end in range(len(str)):
        right_char = str[window_end]
        frequency_map[right_char] += 1

        print(f'window_end = {window_end}, new char = {right_char},  hashmap = {frequency_map}')
        print(f'max_repeat_letter_count = {max_repeat_letter_count}, while freq_map[right_char] = {frequency_map[right_char]}')
        max_repeat_letter_count = max(
            max_repeat_letter_count, 
            frequency_map[right_char]
        )

        # Current window size is from window_start to window_end
        # overall we have a letter which is repeating 
        # 'max_repeat_letter_count' times 
        # this means we can have a window which has one letter
        # repeating 'max_repeat_letter_count' times 
        # and the remaining letters we should replace
        # if the remaining letters are more than k 
        # then it is time to shrink the window as we 
        # are not allowed to repalce more than k letters
        if (window_end - window_start + 1 - max_repeat_letter_count) > k: # if more than k letters, shrink
            left_char = str[window_start]
            frequency_map[left_char] -= 1
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def main():
    print(length_of_longest_substring("aabccbbasdasddsfgt", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()
