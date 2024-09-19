# 2252. 줄 세우기
import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)

        for next in graph[now]:
            indegree[next] -= 1

            if indegree[next] == 0:
                q.append(next)

    return result


N, M = map(int, input().split())

indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

result = []
topology_sort()
print(*result)