def solution(A):
    cA = sorted(A)
    i = 0
    while i < len(cA) - 2:
        
        a = cA[i]
        b = cA[i+1]
        c = cA[i+2]
        
        if a + b > c and b + c > a and a + c > b:
            return 1
        
        i += 1
        
    return 0
