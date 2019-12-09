def permute(nums):
    def gen_sub_permute(sub_nums):
        results = []
        
        if len(sub_nums) == 2:
            return [sub_nums, sub_nums[::-1]]
        else:
            for i in range(len(sub_nums)):
                head = [sub_nums[i]]
                rest = sub_nums[:i] + sub_nums[i+1:]
                sn = gen_sub_permute(rest)
                for ssn in sn:
                    pp = head[:]
                    if type(ssn) is list:
                        pp.extend(ssn)
                    else:
                        pp.append(ssn)
                    pp = "".join(map(str, pp))
                    results.append(pp)
        return results
    
    if len(nums) < 2:
        return [nums]
    
    return gen_sub_permute(nums)

p = sorted(permute(list(range(10))))
print(p[999999])
