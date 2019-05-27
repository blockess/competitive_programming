#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the isValid function below.
def isValid(s):
    # Edget case: no char
    if not s:
        return 'NO'

    counter = Counter(s)
    print(counter)
    values = list(counter.values())
    set_l = len(set(values))
    if set_l <= 2:
        if (set_l) == 1:
            return 'YES'
        else:
            min_=min(values)
            max_=max(values)
            if max_ - min_ == 1:
                if values.count(max_) == 1 or values.count(min_) == 1:
                    return 'YES'
            else:
                if min_ == 1 and values.count(min_) == 1:
                    return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
