import re

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([w for w in reversed(re.split('\s', s)) if w])
