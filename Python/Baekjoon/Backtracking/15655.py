# 15655. N과 M (6)
import sys
input = sys.stdin.readline

def comb(lev, st):
    if lev == M:
        print(*path)
        return
    
    for i in range(st, len(seq)):
        path.append(seq[i])
        comb(lev+1, i+1)
        path.pop()

N, M = map(int, input().split())
seq = sorted(list(map(int, input().split())))

path = []
comb(0, 0)