class Solution:
    def combinationSum(self, candidates, target):
        combinations = []
        if target < 1:
            return []
        
        for n in candidates:
            if n > target:
                continue
                
            if target == n:
                combinations.append([n])
                continue
            
            if n == 1:
                combinations.append([n]*target)
                continue
            
            power = 1
            while target - (n*power) >= 1:
                ccs = self.combinationSum(candidates, target - (n*power))
                for cc in ccs:
                    new_comb = sorted(cc + [n]*power)
                    
                    if new_comb not in combinations:
                        combinations.append(new_comb)

                power += 1    
                
        return combinations
