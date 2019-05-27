import math

def solution(A):
    sum_A = sum(A)
    
    min_diff = math.inf
    left_sum = 0
    right_sum = sum_A
    index = 1
    n = A[0]
    while index < len(A):

        left_sum += n
        right_sum -= n

        min_diff = min(abs(left_sum - right_sum), min_diff)
        n = A[index]
        index += 1
    return min_diff
