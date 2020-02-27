# Tabulation is the opposite of the top-down approach and avoids recursion. 
# In this approach, 
# we solve the problem “bottom-up” 
# (i.e. by solving all the related sub-problems first). 
# This is typically done by filling up an n-dimensional table. 
# Based on the results in the table, 
# the solution to the top/original problem is then computed.
# 
# Tabulation is the opposite of Memoization, 
# as in Memoization we solve the problem and maintain a map of already solved sub-problems. 
# In other words, in memoization, 
# we do it top-down in the sense that we solve the top problem first 
# (which typically recurses down to solve the sub-problems).
# 
# Let’s apply Tabulation to our example of Fibonacci numbers. 
# Since we know that every Fibonacci number is the sum of the two preceding numbers, 
# we can use this fact to populate our table.
# 
# Here is the code for our bottom-up dynamic programming approach:

def calculateFibonacci(n):
    dp = [0, 1]  ## first 2 fib numbers 
    for i in range(2, n+1):
        dp.append(dp[i - 1] + dp[i -2])

    print(n)
    print(dp)
    return dp[n]


def main():
    print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
    print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
    print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))

main()