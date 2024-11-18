# 15651. N과 M (3)
import sys
input = sys.stdin.readline

def perm(lev):
    if lev == M:
        print(*path)
        return

    for i in range(1, N+1):
        path.append(i)
        perm(lev+1)
        path.pop()

N, M = map(int, input().split())
path = []
perm(0)