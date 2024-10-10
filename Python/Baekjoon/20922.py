# 20922. 겹치는 건 싫어
from collections import defaultdict
import sys
input = sys.stdin.readline

def longest_subseq():
    left = 0
    counts = defaultdict(int)
    maxL = 0

    for right in range(N):
        counts[seq[right]] += 1

        while counts[seq[right]] > K:
            counts[seq[left]] -= 1
            if counts[seq[left]] == 0:
                del counts[seq[left]]
            left += 1
        
        maxL = max(maxL, right - left + 1)
    return maxL

N, K = map(int, input().split())
seq = list(map(int, input().split()))
print(longest_subseq())