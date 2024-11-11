# 2644. 촌수계산
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque([(a, 0)])
    visited = [0] * (n+1)
    visited[a] = 1

    while q:
        now, depth = q.popleft()

        if now == b:
            return depth

        for next in graph[now]:
            if visited[next] == 0:
                q.append((next, depth + 1))
                visited[next] = 1
    
    return -1

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs())