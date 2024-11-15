# 4485. 녹색 옷 입은 애가 젤다지?
import heapq
import sys
input = sys.stdin.readline

def dijkstra():
    pq = [(0, (0, 0))]
    cost[0][0] = 0

    while pq:
        now_cost, now = heapq.heappop(pq)
        r, c = now[0], now[1]

        if r == N-1 and c == N-1:
            return cost[r][c]
        
        if now_cost > cost[r][c]:
            continue

        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                new_cost = now_cost + arr[nr][nc]

                if new_cost < cost[nr][nc]:
                    heapq.heappush(pq, (new_cost, (nr, nc)))
                    cost[nr][nc] = new_cost

INF = 1e9
tc = 0
while True:
    tc += 1
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    if N == 0:
        break

    cost = [[INF] * N for _ in range(N)]
    print(f'Problem {tc}: {dijkstra() + arr[0][0]}')