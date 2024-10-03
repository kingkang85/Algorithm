# 1766. 문제집
import sys
import heapq
input = sys.stdin.readline

def topology_sort():
    pq = []

    for i in range(1, N+1):
        if indegree[i] == 0:
            heapq.heappush(pq, i)
    
    while pq:
        now = heapq.heappop(pq)
        result.append(now)

        for next in graph[now]:
            indegree[next] -= 1

            if indegree[next] == 0:
                heapq.heappush(pq, next)

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