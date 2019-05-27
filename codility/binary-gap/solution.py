def solution(N):
    n_str = str(bin(N))[2:]
    max_gap = 0
    current_gap = 0
    is_open = False
    for s in n_str:
        if s == '1':
            if current_gap > 0:
                max_gap = max(max_gap, current_gap)
                current_gap = 0
            else:
                is_open = True
        else:
            if is_open:
                current_gap += 1
            
    return max_gap
