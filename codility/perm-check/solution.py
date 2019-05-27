def solution(A):
    sorted_A = sorted(A)
    
    for i,n in enumerate(sorted_A):
        if n != i+1:
            return 0
    return 1
