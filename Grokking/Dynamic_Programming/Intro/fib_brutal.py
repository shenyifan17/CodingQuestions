def calFib_brutal(n):
    if n < 2:
        return n 
    return calFib_brutal(n-1) + calFib_brutal(n-2)

def main():

    print("5th fib is " + str(calFib_brutal(5)))
    print("6th fib is " + str(calFib_brutal(6)))
    print("10th fib is " + str(calFib_brutal(10)))

main()

## As we saw above, 
# this problem shows the overlapping subproblems pattern, 
# so let’s make use of memoization here. 
# We can use an array to store the already solved subproblems 