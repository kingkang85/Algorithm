# 1966. 프린터 큐
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    q = [(int(input()), i) for i in range(N)]

    q.pop(0)