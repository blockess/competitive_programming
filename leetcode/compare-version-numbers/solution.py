class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        subversions1 = version1.split('.')
        subversions2 = version2.split('.')
        len_sv1 = len(subversions1)
        len_sv2 = len(subversions2)
        
        if len_sv1 < len_sv2:
            subversions1.extend(["0"]*(len_sv2-len_sv1))
        elif len_sv2 < len_sv1:
            subversions2.extend(["0"]*(len_sv1-len_sv2))
            
        for s1,s2 in zip(subversions1, subversions2):
            v1 = s1.lstrip('0')
            v2 = s2.lstrip('0')
            
            if not v1:
                v1 = 0
            if not v2:
                v2 = 0
                
            v1 = int(v1)
            v2 = int(v2)
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
            
        return 0
