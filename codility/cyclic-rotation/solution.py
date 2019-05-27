def solution(A, K):
    if not A:
        return A
        
    len_A = len(A)
    new_A = [0]*len_A
    if len(set(A)) == 1:
        return A
    if len_A == K:
        return A
    for i,n in enumerate(A):
        next_index = (K + i) % len_A
        new_A[next_index] = A[i]
        
    return new_A
