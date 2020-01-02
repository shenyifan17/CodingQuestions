""""
Given length n and number of ones k
return all permutations of 0, 1

e.g. 
n = 4, k = 3
returns ['1110', '1101', '1011', '0111'] 
"""

def combinations(iterable, r):
    # combinations('ABCD', 2) -- > AB, AC, AD, BC, BD, CD
    # combinations(range(4), 3) -- > 012 013 023 123  
    # this returns all the posibilities of nCk
    """"
    Return r length subsequences of elements from the input iterable.
    This is the same as itertools.combinations 

    Returns position for kbits 

    The number of items returned is n! / r! / (n-r)! when 0 <= r <= n or zero when r > n.
    """
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return 
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break 
        else: 
            return 
        indices[i] += 1 
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1 
        yield tuple(pool[i] for i in indices)

def kbits(n, k):
    """"
    Generate permutations
    """
    result = []
    for bits in combinations(range(n), k):
        print(bits)
        s = ['0'] * n 
        for bit in bits:
            s[bit] = '1'
        result.append(''.join(s))
    return result 

if __name__ == '__main__':
    print(kbits(2,1))
    print(kbits(3,1))
    print(kbits(4,1))
    print(kbits(5,4))
    print(kbits(6,6))