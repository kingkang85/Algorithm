# 15652. N과 M (4)
import sys
input = sys.stdin.readline

def perm(lev, st):
    if lev == M:
        print(*path)
        return
    
    for i in range(st, N+1):
        path.append(i)
        perm(lev + 1, i)
        path.pop()

N, M = map(int, input().split())
path = []
perm(0, 1)