def solution(A, B):
    upstream_stack = []
    survivors = 0
    for w,d in zip(A,B):
        if d == 0:
            if upstream_stack:
                while upstream_stack:
                    f = upstream_stack[-1]
                    if f < w:
                        upstream_stack.pop()
                        if not upstream_stack:
                            survivors += 1
                    else:
                        break
            else:
                survivors += 1
        else:
            upstream_stack.append(w)
    
    survivors += len(upstream_stack)
    return survivors
