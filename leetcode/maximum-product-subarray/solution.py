# Solution 1

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if not len_nums:
            return 0

        if len_nums == 1:
            return nums[0]

        max_products = [nums[0]]
        min_products = [nums[0]]

        for i,n in enumerate(nums):
            if i == 0:
                continue

            max_product = max(n, n*max_products[i-1])
            max_product = max(max_product, n*min_products[i-1])
            min_product = min(n, n*min_products[i-1])
            min_product = min(min_product, n*max_products[i-1])

            max_products.append(max_product)
            min_products.append(min_product)

        return sorted(max_products)[-1]

# Solution 2

from operator import mul
from functools import reduce

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        def product(array):
            return reduce(mul, array, 1)

        cum_subarray = []
        cur_subarray = []
        neg_indexes = []
        max_product = max(nums)
        for num in nums:
            if num == 0:
                if cur_subarray:
                    meta_subarray = dict(
                        subarray=cur_subarray,
                        neg_indexes=neg_indexes
                    )
                    cum_subarray.append(meta_subarray)
                neg_indexes = []
                cur_subarray = []
            elif num < 0:
                neg_indexes.append(len(cur_subarray))
                cur_subarray.append(num)
            else:
                cur_subarray.append(num)
        if cur_subarray:
            meta_subarray = dict(
                subarray=cur_subarray,
                neg_indexes=neg_indexes
            )
            cum_subarray.append(meta_subarray)

        for c_subarray in cum_subarray:
            if len(c_subarray['subarray']) == 1 and c_subarray['neg_indexes'] == 1:
                continue

            neg_indexes = c_subarray['neg_indexes']
            subarray = c_subarray['subarray']
            len_sa = len(subarray)
            if len(neg_indexes) % 2 == 0:
                max_product = max(max_product, product(subarray))
            else:
                for i in range(len_sa):
                    for j in range(i+1, len_sa+1):
                        max_product = max(max_product, product(subarray[i:j]))

        return max_product
