# 15663. N과 M (9)
import sys
input = sys.stdin.readline

def perm(lev):
    if lev == M:
        print(*path)
        return

    last = -1
    for i in range(len(seq)):
        if not used[i] and seq[i] != last:
            path.append(seq[i])
            used[i] = 1
            last = seq[i]
            perm(lev+1)
            path.pop()
            used[i] = 0
    

N, M = map(int, input().split())
seq = sorted(list(map(int, input().split())))

path = []
used = [0] * (len(seq))
perm(0)