# 16398. 행성 연결
import sys
input = sys.stdin.readline

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    px = find(x)
    py = find(y)

    if px < py:
        p[py] = px
    else:
        p[px] = py

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

edges = []
for i in range(N):
    for j in range(i+1, N):
        edges.append((i+1, j+1, arr[i][j]))

edges.sort(key = lambda x: x[2])

p = [i for i in range(N+1)]

sumV = 0
for a, b, cost in edges:
    if find(a) != find(b):
        union(a, b)
        sumV += cost

print(sumV)