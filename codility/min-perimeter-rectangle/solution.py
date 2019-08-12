def solution(N):
    lf = 1
    i = 1
    
    while i * i <= N:
        if N % i == 0:
            lf = i
        i += 1
    
    return 2 * (lf + (N//lf))
