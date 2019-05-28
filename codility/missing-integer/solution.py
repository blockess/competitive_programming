
# O(N + M)

def solution(A):
    len_A= len(A)
    counter = [0]*(len_A+1)
    for n in A:
        if 0 < n <= len_A:
            counter[n-1] = 1
    for i in range(len_A+1):
        if counter[i] == 0:
            return i + 1

# O(N * log(N))

from collections import defaultdict

def solution(A):
    sorted_A = sorted(A)

    min_ = 1
    for n in sorted_A:
        if n < 1:
            continue

        if n == min_:
            min_ += 1
            continue
    return min_
