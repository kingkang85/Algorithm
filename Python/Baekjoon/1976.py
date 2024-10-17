# 1976. 여행 가자
# BFS 이용
# from collections import deque
# import sys
# input = sys.stdin.readline

# def bfs(start, end):
#     q = deque([start])
#     visited = [0] * (N+1)
#     visited[start] = 1

#     while q:
#         now = q.popleft()
#         if now == end:
#             return True
        
#         for next in graph[now]:
#             if visited[next] == 0:
#                 q.append(next)
#                 visited[next] = 1

#     return False

# N = int(input().strip())
# M = int(input().strip())

# graph = [[] for _ in range(N+1)]
# for i in range(N):
#     lst = list(map(int, input().split()))
#     for j in range(N):
#         if lst[j] == 1:
#             graph[i+1].append(j+1)

# cities = list(map(int, input().split()))

# for i in range(M-1):
#     if not bfs(cities[i], cities[i+1]):
#         print('NO')
#         break
# else:
#     print('YES')

####################################################################################
# Union-Find 이용
import sys
input = sys.stdin.readline

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    pa = find(a)
    pb = find(b)

    if rank[pa] < rank[pb]:
        p[pa] = pb
    elif rank[pa] > rank[pb]:
        p[pb] = pa
    else:
        p[b] = pa
        rank[pa] += 1

N = int(input())
M = int(input())

p = [i for i in range(N+1)]
rank = [0] * (N+1)

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            union(i+1, j+1)

cities = list(map(int, input().split()))

result = set(find(city) for city in cities)
if len(result) == 1:
    print('YES')
else:
    print('NO')