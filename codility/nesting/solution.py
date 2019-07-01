def solution(S):
    stack = []
    for s in S:
        if s == '(':
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                return 0
        
    if stack:
        return 0
    else:
        return 1
