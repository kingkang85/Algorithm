# 2178. 미로 탐색
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    visited = [[0] * M for _ in range(N)]
    q = deque([(0, 0, 1)])
    visited[0][0] = 1

    while q:
        r, c, dist = q.popleft()

        if r == N-1 and c == M-1:
            return dist
        
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == '1':
                q.append((nr, nc, dist+1))
                visited[nr][nc] = 1


N, M = map(int, input().split())
arr = [input() for _ in range(N)]
print(bfs())
