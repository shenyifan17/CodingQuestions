# Write a function that, given two integers A and B, returns the number of 
# integers from [A, B] which can be expressed as the product of two consequtive 
# integers X * (X+1)

import math

## Slow: 
def solution_1(A,B):

    def check_product(n):
        i = int(math.sqrt(n))
        return 1 if (i*(i+1))==n else 0

    all_numbers = list(range(A,B+1))
    return sum(list(map(check_product, all_numbers)))

## Fast from LTC 
import numpy as np
def solution_2(A, B):
    # Analytical solution, complexity O(1)

    # Solve x(x+1) = y 
    def getRoot(y):
        return (-1 + np.sqrt(1 + 4 * y)) / 2.0
    
    root1, root2 = getRoot(A), getRoot(B)
    
    lower_bound = int(root1 - 1)
    upper_bound = int(root2 + 1)
    #lower_bound / upper_bound off at most by 1
    print(f"pre root1={root1} root2={root2} lower_bound={lower_bound} upper_bound={upper_bound}")

    while lower_bound <= upper_bound:
        if lower_bound * (lower_bound+1) < A:
            lower_bound += 1
        else:
            break
    while lower_bound <= upper_bound:
        if upper_bound * (upper_bound+1) > B:
            upper_bound -= 1
        else:
            break
    #print(f"post root1={root1} root2={root2} lower_bound={lower_bound} upper_bound={upper_bound}")
    return upper_bound - lower_bound + 1
        

