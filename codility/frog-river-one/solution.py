def solution(X, A):
    leaves = [None]*X
    missing_leaves = X
    for i,leaf in enumerate(A):
        if leaf > X:
            continue
        
        if leaves[leaf-1] is None:
            leaves[leaf-1] = i
            missing_leaves -= 1
        
        if missing_leaves == 0:
            return max(leaves)
        
    return -1
