OPS = ['/', '+', '-', '*']

import re

class Solution:
    def compute(self, a, op, b):
        flip = False
        if a < 0:
            flip = True
        if op == '/':
            res = abs(a) // b
            if flip:
                return res * -1
            else:
                return res
        elif op == '*':
            return a * b
            
    def calculate(self, s: str) -> int:
        s += "+0"
        stack = []
        len_s = len(s)
        num = ''
        index = 1
        el = s[0]
        flag_compute = False
        last_op = ''
        while index < len_s:
            if el == ' ':
                el = s[index]
                index += 1
            
            if el:
                if el in OPS:                 
                    if num:
                        if last_op == '-':
                            num = int(num) * -1
                        stack.append(int(num))
                        num = ''
                        
                    if flag_compute:
                        res = self.compute(stack[-2], flag_compute, stack[-1])
                        stack = stack[:-2] + [res]
                        flag_compute = ''

                    if el in ['/', '*']:
                        flag_compute = el
                    last_op = el
                else:
                    num += el
                
            if index < len_s - 1:
                el = s[index]
            index+=1
        return sum(stack)
