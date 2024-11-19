# 15656. N과 M (7)
import sys
input = sys.stdin.readline

def perm(lev):
    if lev == M:
        print(*path)
        return
    
    for i in range(0, len(seq)):
        path.append(seq[i])
        perm(lev+1)
        path.pop()

N, M = map(int, input().split())
seq = sorted(list(map(int, input().split())))

path = []
perm(0)