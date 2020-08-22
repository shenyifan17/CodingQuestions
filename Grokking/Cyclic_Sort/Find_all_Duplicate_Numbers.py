# Problem Statement #
# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
# The array has some duplicates, find all the duplicate numbers without using any extra space.
#
# Example 1:
#
# Input: [3, 4, 4, 5, 5]
# Output: [4, 5]
# Example 2:
#
# Input: [5, 4, 7, 2, 3, 5, 3]
# Output: [3, 5]

def find_all_duplicates(nums):
    print(' ----------- START -----------')
    print(nums)
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        print(f'i = {i}, j = {j}')
        print(f'j = nums[i] - 1 = {nums[i]} - 1 = {j}')
        print(f'nums[{i}] = {nums[i]}, nums[{j}] = {nums[j]}')
        if nums[i] != nums[j]:
            print('nums[i] != nums[j], SWAP')
            nums[i], nums[j] = nums[j], nums[i] # SWAP
        else:
            i += 1
        print(nums)

    duplicateNumbers = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicateNumbers.append(nums[i])

    return duplicateNumbers

def main():
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


main()


# Time comp O(n)
# Space comp O(1)