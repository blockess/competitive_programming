def solution(H):
    final_stack = []
    curr_stack = [H[0]]
    for h in H[1:]:
        if h == curr_stack[-1]:
            continue
        elif h < curr_stack[-1]:
            while True:
                if curr_stack:
                    if h < curr_stack[-1]:
                        final_stack.append(curr_stack.pop())
                        continue
                
                break
            if curr_stack:
                if curr_stack[-1] != h:
                    curr_stack.append(h)
            else:
                curr_stack = [h]
        else:
            curr_stack.append(h)
    
    final_stack.extend(curr_stack)
    return len(final_stack)
