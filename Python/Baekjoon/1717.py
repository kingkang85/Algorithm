# 1717. 집합의 표현
import sys
input = sys.stdin.readline

def Find(x):
    if x != p[x]:
        p[x] = Find(p[x])
    return p[x]

def Union(x, y):
    px = Find(x)
    py = Find(y)

    if px != py:
        if rank[px] < rank[py]:
            p[px] = py
        elif rank[px] > rank[py]:
            p[py] = px
        else:
            p[px] = py
            rank[py] += 1


N, M = map(int, input().split())

p = [i for i in range(N+1)]
rank = [0] * (N+1)
for _ in range(M):
    c, a, b = map(int, input().split())

    if c == 0:
        Union(a, b)
    
    else:
        if Find(a) != Find(b):
            print('NO')
        else:
            print('YES')