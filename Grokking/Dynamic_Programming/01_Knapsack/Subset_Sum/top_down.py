def can_partition(num):
    """"
    num (list)
    """
    s = sum(num)

    # if "s" is odd, we cant have subsets with equal sum 
    if s % 2 != 0:
        return False 

    # initialize the "dp" array, 
    # -1 for defaul, 1 for True and 0 for False
    dp = [[-1 for x in range(int(s/2)+1)] for u in range(len(num))]

    if can_partition_recursive(dp, num, int(s/2), 0) == 1:
        return True
    else: 
        return False 

def can_partition_recursive(dp, num, sum, currentIndex):
    # base check 
    if sum == 0: ## recursion of reducing "sum" to 0
        return 1 
    
    n = len(num)
    if (n==0) or (currentIndex>=n):
        return 0

    # if we ahve not already processed a similar problem
    if dp[currentIndex][sum] == -1:
        # recursive call after choosing the number at the 
        # currentIndex
        if num[currentIndex] <= sum:
            if can_partition_recursive(dp, num,
                                       sum-num[currentIndex],
                                       currentIndex+1) == 1:
                dp[currentIndex][sum] == 1
                return 1

        # recursive call after excluding the numebr at the 
        # currentIndex
        dp[currentIndex][sum] = can_partition_recursive(
            dp, num, sum, currentIndex+1
        )
    
    return dp[currentIndex][sum]
                

def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))

main()


## Time comp and Space comp: O(N*S)
## where N is total number of numbers, and 
## S is the total sum of all numbers 