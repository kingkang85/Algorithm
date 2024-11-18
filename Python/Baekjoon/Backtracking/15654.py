# 15654. N과 M (5)
import sys
input = sys.stdin.readline

def perm(lev):
    if lev == M:
        print(*path)
        return
    
    for num in seq:
        if not used[num]:
            path.append(num)
            used[num] = 1
            perm(lev+1)
            path.pop()
            used[num] = 0

    
N, M = map(int, input().split())
seq = sorted(list(map(int, input().split())))

path = []
used = [0] * (seq[-1]+1)
perm(0)