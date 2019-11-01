class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
                        results.append(head+ssn)
            return results
        
        if len(nums) < 2:
            return [nums]
        
        return gen_sub_permute(nums)
