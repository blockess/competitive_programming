import operator
from collections import defaultdict

def solution(A):
    equi_leader = 0
    lc = defaultdict(lambda: 0)
    rc = defaultdict(lambda: 0)
    
    for a in A:
        rc[a] += 1
    
    dominator = sorted(rc.items(), key=operator.itemgetter(1), reverse=True)[0][0]
    if rc[dominator] < sum(rc.values()) // 2:
        return 0
    
    for a in A:
        lc[a] += 1
        rc[a] -= 1
        hlc = sum(lc.values()) // 2
        hrc = sum(rc.values()) // 2
        
        dlc = sorted(lc.items(), key=operator.itemgetter(1), reverse=True)[0][0]
        drc = sorted(rc.items(), key=operator.itemgetter(1), reverse=True)[0][0]
            
        if lc[dlc] > hlc and rc[drc] > hrc and dlc == dominator and drc == dominator:
            equi_leader += 1
            
    return equi_leader
