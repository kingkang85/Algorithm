# 1916. 최소비용 구하기
import heapq
import sys
input = sys.stdin.readline

def Dijkstra(start, end):
    pq = [(0, start)]  # (비용, 출발점)
    cost = [1e9] * (N+1)
    cost[start] = 0

    while pq:
        c, now = heapq.heappop(pq)

        if c > cost[now]:
            continue
        
        # 도착점에 도착하면 최소 비용 출력
        if now == end:
            return c

        for new_c, next in graph[now]:
            new_cost = c + new_c

            if new_cost < cost[next]:
                heapq.heappush(pq, (new_cost, next))
                cost[next] = new_cost
                

N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수

graph = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2, w = map(int, input().split())
    graph[n1].append((w, n2))  # 비용, 도착 도시 번호 순으로 저장

start, end = map(int, input().split())
print(Dijkstra(start, end))