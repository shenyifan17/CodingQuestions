# Problem Statement #
# We are given an unsorted array containing ‘n+1’ numbers taken
# from the range 1 to ‘n’.
# The array has only one duplicate but it can be repeated multiple times.
# Find that duplicate number without using any extra space.
# You are, however, allowed to modify the input array.
#
# Example 1:
#
# Input: [1, 4, 4, 3, 2]
# Output: 4
# Example 2:
#
# Input: [2, 1, 3, 3, 5, 4]
# Output: 3
# Example 3:
#
# Input: [2, 4, 1, 4, 4]
# Output: 4

# This problem follows Cyclic Sort pattern and shares similarities with
# Find the Missing Number. Follow a similar approach, we will try to place each number on its correct index
# Since there is only one duplicate, if while swapping the number with its index both the numbers being
# swapped are the same, we then have found the duplicate

def find_duplicate(nums):
    i = 0
    print('-------- START ---------')
    while i < len(nums):
        print(f'i = {i}, nums = {nums}')
        if nums[i] != i + 1:
            j = nums[i] - 1
            print(f'j = nums[i] - 1 = {nums[i]} - 1 = {j}')
            print(f'nums[{i}] = {nums[i]}, nums[{j}] = {nums[j]}')
            if nums[i] != nums[j]:
                print('SWAP')
                nums[i], nums[j] = nums[j], nums[i] # SWAP
            else: # we have found the duplicate
                print('nums[i] = nums[j], we have found the duplicate')
                return nums[i]
        else:
            i += 1

    return -1


def main():
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 4, 1, 4, 4]))


main()

# Time complexity O(n)
# Space complexity O(1)

## NOTE Solution 2 using fast and slow pointers, see
# FAST AND SLOW POINTER folder