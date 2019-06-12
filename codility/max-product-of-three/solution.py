# Solution 1

# O(n log(n))

from functools import reduce

def solution(A):
    
    def mul(l):
        return reduce(lambda x,y: x * y, l)
    
    sorted_A = sorted(A)
    
    return max(mul(sorted_A[:2]+sorted_A[-1:]), mul(sorted_A[-3:]))

# O(n)

import math

def solution(A):
    max_ = [-math.inf, -math.inf, -math.inf]
    min_ = [math.inf, math.inf]

    for n in A:
        if n >= max_[2]:
            max_[0] = max_[1]
            max_[1] = max_[2]
            max_[2] = n
        elif n >= max_[1]:
            max_[0] = max_[1]
            max_[1] = n
        elif n >= max_[0]:
            max_[0] = n

        if n <= min_[1]:
            min_[0] = min_[1]
            min_[1] = n
        elif n <= min_[0]:
            min_[0] = n

    return max(min_[0] * min_[1] * max_[2], max_[0] * max_[1] * max_[2])
