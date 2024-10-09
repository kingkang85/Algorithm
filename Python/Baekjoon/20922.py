# 20922. 겹치는 건 싫어
from collections import defaultdict
import sys
input = sys.stdin.readline

def longest_subseq():
    counts = defaultdict(int)
    left = 0
    max_length = 0

    for right in range(N):
        counts[seq[right]] += 1

        while counts[seq[right]] > K:
            counts[seq[left]] -= 1
            if counts[seq[left]] == 0:
                del counts[seq[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

N, K = map(int, input().split())
seq = list(map(int, input().split()))

print(longest_subseq())
