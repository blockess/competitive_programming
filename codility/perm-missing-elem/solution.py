def solution(A):
    ubound = len(A)+1
    target_sum = ubound * (ubound+1) // 2
    actual_sum = sum(A)
    return target_sum - actual_sum
