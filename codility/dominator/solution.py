from collections import defaultdict

def solution(A):
    indexer = defaultdict(list)
    threshold = (len(A) // 2) + 1
    
    for i,a in enumerate(A):
        indexer[a].append(i)
        if len(indexer[a]) == threshold:
            return i
    
    return -1
