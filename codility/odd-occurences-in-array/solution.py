def solution(A):
    sorted_A = sorted(A)
    
    index = 0
    while index < len(sorted_A) -1:
        n=sorted_A[index]
        m=sorted_A[index+1]
        if n != m:
            return n
        index += 2
    
    return sorted_A[-1]
