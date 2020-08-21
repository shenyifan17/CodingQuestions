# Problem Statement #
# We are given an array containing ‘n’ objects. Each object, when created,
# was assigned a unique number from 1 to ‘n’ based on their creation sequence.
# This means that the object with sequence number ‘3’ was created just before the
# object with sequence number ‘4’.
#
# Write a function to sort the objects in-place on their creation sequence number in
# O(n) and without any extra space.
# For simplicity, let’s assume we are passed an integer array containing only the sequence numbers,
# though each number is actually an object.
#
# Example 1:
#
# Input: [3, 1, 5, 4, 2]
# Output: [1, 2, 3, 4, 5]
# Example 2:
#
# Input: [2, 6, 4, 3, 1, 5]
# Output: [1, 2, 3, 4, 5, 6]
# Example 3:
#
# Input: [1, 5, 6, 4, 3, 2]
# Output: [1, 2, 3, 4, 5, 6]

# Solution:
# we iterate the array one number at a time,
# and if the current number we are iterating is not at the correct index,
# we swap it with the number at its correct index.
# This way we will go through all numbers and place them in their correct indices,
# hence, sorting the whole array.

def cyclic_sort(nums):
    i = 0
    print('----------- START ----------- ')
    print(nums)
    while i < len(nums):
        j = nums[i] - 1
        print(f'i = {i}, j = {j}')
        if nums[i] != nums[j]:
            print(f'nums[{i}] = {nums[i]}, nums[{j}] = {nums[j]}, SWAP')
            nums[i], nums[j] = nums[j], nums[i] # swap
        else:
            print(f'nums[{i}] = {nums[i]}, nums[{j}] = {nums[j]}, NO SWAP, i += 1')
            i +=1
        print(nums)
    return nums

def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()

# Time complexity #
# The time complexity of the above algorithm is O(n).
# Although we are not incrementing the index i when swapping the numbers,
# this will result in more than ‘n’ iterations of the loop,
# but in the worst-case scenario,
# the while loop will swap a total of ‘n-1’ numbers and once a number is at its correct index,
# we will move on to the next number by incrementing i.
# So overall, our algorithm will take O(n) + O(n-1) which is asymptotically equivalent to O(n).
#
# Space complexity #
# The algorithm runs in constant space O(1)O(1).

