# Solution #
# The process, defined above, to find out if a number is a happy number or not, 
# always ends in a cycle. 
# If the number is a happy number, 
# the process will be stuck in a cycle on number ‘1,’ 
# and if the number is not a happy number,
# then the process will be stuck in a cycle with a set of numbers. 
# As we saw in Example-2 while determining if ‘12’ is a happy number or not, 
# our process will get stuck in a cycle with the following numbers: 
# 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
# 
# We saw in the LinkedList Cycle problem that we can use the 
# Fast & Slow pointers method to find a cycle among a set of elements. 
# As we have described above, each number will definitely have a cycle. 
# Therefore, 
# we will use the same fast & slow pointer strategy to find the cycle and once the cycle is found, 
# we will see if the cycle is stuck on number ‘1’ to find out if the number is happy or not.

def find_happy_number(num):

    slow, fast = num, num 
    while True: 
        slow = find_square_sum(slow) # move one step 
        fast = find_square_sum(find_square_sum(fast)) # move two steps 
        if slow == fast: ## find the cycle 
            break 
    return slow == 1 # see if the cycle is stuck on number '1'

def find_square_sum(num):

    _sum = 0 
    while (num > 0):
        digit = num % 10 
        _sum += digit * digit 
        num = num // 10 ## also num //= 10 
    return _sum

def main():
    print(find_happy_number(23))
    print(find_happy_number(12))
    print(find_happy_number(54))
    print(find_happy_number(82))

main()

