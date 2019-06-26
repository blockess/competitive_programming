def solution(S):
    stack = []
    PAREN_PAIRS = {')': '(', ']': '[', '}': '{'}
    for s in S:
        if s in PAREN_PAIRS.keys():
            try:
                last_s = stack.pop()
            except IndexError:
                return 0
            if last_s != PAREN_PAIRS[s]:
                return 0
        elif s in PAREN_PAIRS.values():
            stack.append(s)
    
    if stack:
        return 0
    return 1
