# My "clever" solution

from collections import defaultdict

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ll = defaultdict(lambda: [])
        max_l = 0
        for n in nums:
            max_l = max(max_l, len(str(n)))

        for n in nums:
            str_n = str(n)
            if len(str_n) < max_l:
                repeat = max_l//len(str_n) + 1
                key = (str_n*repeat)[:max_l]
            else:
                key = str_n

            if len(ll[key]) > 0:
                prepend = str_n + ''.join(ll[key])
                append = ''.join(ll[key]) + str_n
                if int(prepend) > int(append):
                    ll[key].insert(0, str_n)
                else:
                    ll[key].append(str_n)
            else:
                ll[key].append(str_n)

        answer = ''
        for l in sorted(ll.keys(), reverse=True):
            answer += ''.join(ll[l])

        if answer[0] == '0':
            return '0'

        return answer

# Proper solution with Proof
"""
We use a.b to represent the concatenation of non-negative integers a and b .

Theorem:

Let a, b, and c be non-negative integers. If a.b > b.a and b.c > c.b , we have a.c > c.a .

Proof:

We use [a] to denote the length of the decimal representation of a . For example, if a = 10 , we have [a] = 2 .

Since a.b > b.a and b.c > c.b , we have

a * 10^[b] + b > b * 10^[a] + a
b * 10^[c] + c > c * 10^[b] + b

, which is equivalent to

a * (10^[b] - 1) > b * (10^[a] - 1)
b * (10^[c] - 1) > c * (10^[b] - 1)

Obviously, 10^[a] - 1 > 0 , 10^[b] - 1 > 0 , and 10^[c] - 1 > 0 . Since c >= 0 , according to the above inequalities, we know that b > 0 and a > 0 . After multiplying the above two inequalities and cancelling b and (10^[b] - 1) , we have

a * (10^[c] - 1) > c * (10^[a] - 1)

This is equivalent to

a * 10^[c] + c > c * 10^[a] + a

, which means a.c > c.a .

Q.E.D.
"""

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(n1,n2):
            n1_n2 = n1 + n2
            n2_n1 = n2 + n1
            if n1_n2 > n2_n1:
                return 1
            else:
                if n1_n2 < n2_n1:
                    return -1

            return 0

        nums = [str(n) for n in nums]
        nums.sort(key=cmp_to_key(compare), reverse=True)

        answer = ''.join(nums)
        if answer[0] == '0':
            return '0'

        return answer
