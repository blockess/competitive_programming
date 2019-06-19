#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    alice_ranks = []
    
    scores.append(-math.inf)
    rank = i = last_score = 0
    for alice_score in reversed(alice):
        while i < len(scores):
            score = scores[i]
            if score <= alice_score:
                alice_ranks.append(rank+1)
                break
            else:
                i += 1
                if last_score != score:
                    rank += 1
            last_score = score

    return reversed(alice_ranks)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
