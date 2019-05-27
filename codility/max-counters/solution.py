def solution(N, A):
    el_counter = [0]*N
    max_counter = base_counter = 0
    for n in A:
        if n > N:
            base_counter = max_counter
            continue
        
        i = n-1
        if el_counter[i] < base_counter:
            el_counter[i] = base_counter + 1
        else:
            el_counter[i] += 1

        max_counter = max(el_counter[i],max_counter)
    
    answer = [0]*N
    for i in range(N):
        answer[i] = el_counter[i]
        if answer[i] < base_counter:
            answer[i] = base_counter
            
    return answer
