# 1647. 도시 분할 계획
import sys
input = sys.stdin.readline

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px != py:
        if rank[px] > rank[py]:
            p[py] = px
        elif rank[px] < rank[py]:
            p[px] = py     
        else:
            p[py] = px
            rank[px] += 1


N, M = map(int, input().split())

edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

edges.sort(key = lambda x: x[2])

p = [i for i in range(N+1)]
rank = [0] * (N+1)
ans = 0  # 연결된 마을 길이의 합
last_edge = 0  # 마지막에 연결된 마을 길이
for edge in edges:
    s, e, w = edge
    if find_set(s) != find_set(e):
        union(s, e)
        ans += w
        last_edge = w

print(ans - last_edge)