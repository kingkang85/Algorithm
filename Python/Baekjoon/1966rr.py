# 1966. 프린터 큐
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    docs = deque([(i,) for i in range(N)])
    priority = list(map(int, input().split()))
    for i in range(N):
        docs[i] += (priority[i],)

    
    