# 1922. 네트워크 연결
def Find(x):
    if x != p[x]:
        p[x] = Find(p[x])
    return p[x]

def Union(x, y):
    px = Find(x)
    py = Find(y)

    if px != py:
        if rank[px] > rank[py]:
            p[py] = px
        elif rank[px] < rank[py]:
            p[px] = py
        else:
            p[py] = px
            rank[px] += 1


N = int(input())
M = int(input())

edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key = lambda x: x[2])

p = [i for i in range(N+1)]
rank = [0] * (N+1)
result = 0
for s, e, w in edges:
    if Find(s) != Find(e):
        Union(s, e)
        result += w

print(result)