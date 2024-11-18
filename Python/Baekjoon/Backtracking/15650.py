# 15650. N과 M (2)
import sys
input = sys.stdin.readline

def comb(lev, st):
    if lev == M:
        print(*path)

    for i in range(st, N+1):
        path.append(i)
        comb(lev+1, i+1)
        path.pop()

N, M = map(int, input().split())
path = []
comb(0, 1)