# 14940. 쉬운 최단거리
from collections import deque
import sys
input = sys.stdin.readline

def find_start():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                continue
            if arr[i][j] == 2:
                sti, stj = i, j  # 목표 지점에서 출발
            result[i][j] = 0
    return sti, stj

def bfs(sti, stj):
    q = deque([(sti, stj, 0)])
    visited = [[0] * M for _ in range(N)]
    visited[sti][stj] = 1
    
    while q:
        i, j, dist = q.popleft()

        for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj, dist + 1))
                visited[ni][nj] = 1
                result[ni][nj] = dist + 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = [[-1] * M for _ in range(N)]
sti, stj = find_start()
bfs(sti, stj)

for row in result:
    print(*row)