# 2606. 바이러스
from collections import deque
import sys
input = sys.stdin.readline

def bfs(st):
    q = deque([st])
    visited[st] = 1

    cnt = 0
    while q:
        now = q.popleft()

        for next in graph[now]:
            if visited[next] == 0:
                q.append(next)
                visited[next] = 1
                cnt += 1
                
    return cnt

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)
print(bfs(1))