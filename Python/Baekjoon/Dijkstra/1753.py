# 1753. 최단경로
import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(st):
    pq = []
    distance[st] = 0
    heapq.heappush(pq, (0, st))

    while pq:
        cost, now = heapq.heappop(pq)

        if distance[now] < cost:
            continue

        for next_node, next_cost in graph[now]:
            new_cost = cost + next_cost
            if new_cost < distance[next_node]:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = [INF] * (V+1)
dijkstra(K)

for d in distance[1:]:
    if d == INF:
        print('INF')
    else:
        print(d)