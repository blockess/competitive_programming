def prefix_sum(A,n):
    ps = [0] * (n + 1)
    for i in range(1, n + 1):
        ps[i] = ps[i-1] + A[i-1]
    return ps

def solution(A):
    len_A = len(A)
    ps = prefix_sum(A, len_A)
    pairs = 0
    lps = ps[-1]
    for i,n in enumerate(A):
        if pairs > 1000000000:
            return -1
        if n == 0:
            pairs += lps - ps[i]
        
    return pairs
